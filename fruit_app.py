import streamlit as st
import torch
from torchvision import transforms, models
from PIL import Image

# === Constants ===
MODEL_PATH = 'best_fruit_model.pt'
IMAGE_SIZE = 224
CLASS_NAMES = ['Apple', 'Banana', 'Grapes', 'Guava', 'Mango',
               'Orange', 'Papaya', 'Pomegranate', 'Strawberry', 'Watermelon']

# === Device ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# === Transform (same as validation) ===
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# === Load model ===
@st.cache_resource
def load_model():
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Sequential(
        torch.nn.Linear(model.fc.in_features, 256),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.3),
        torch.nn.Linear(256, len(CLASS_NAMES))
    )
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.to(device)
    model.eval()
    return model

model = load_model()

# === Streamlit UI ===
# Sidebar with info and instructions
st.sidebar.title("🍉 Fruit Classifier App")
st.sidebar.markdown("""
Welcome to the Fruit Classifier! 🍎🍌🍇\n\nUpload a clear image of a fruit and let our AI model predict which fruit it is.\n\n**Supported Fruits:**\n- Apple\n- Banana\n- Grapes\n- Guava\n- Mango\n- Orange\n- Papaya\n- Pomegranate\n- Strawberry\n- Watermelon\n\n*Model: ResNet18, PyTorch*\n""")

st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        color: white;
        background: linear-gradient(90deg, #ffb347 0%, #ffcc33 100%);
        border-radius: 8px;
        font-size: 18px;
        padding: 0.5em 2em;
    }
    .stFileUploader>div>div {
        background-color: #fffbe7;
        border-radius: 8px;
        padding: 1em;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍎 Fruit Classifier")
st.write(":sparkles: **Upload an image of a fruit and let the model guess what it is!** :sparkles:")

# Center the uploader and results
col1, col2, col3 = st.columns([1,2,1])
with col2:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("")
        with st.spinner('Analyzing the image...'):
            # Preprocess
            input_tensor = transform(image).unsqueeze(0).to(device)
            # Inference
            with torch.no_grad():
                output = model(input_tensor)
                pred_idx = output.argmax(1).item()
                pred_class = CLASS_NAMES[pred_idx]
        fruit_emojis = {
            'Apple': '🍎',
            'Banana': '🍌',
            'Grapes': '🍇',
            'Guava': '🥝',
            'Mango': '🥭',
            'Orange': '🍊',
            'Papaya': '🧡',
            'Pomegranate': '🍈',
            'Strawberry': '🍓',
            'Watermelon': '🍉',
        }
        emoji = fruit_emojis.get(pred_class, '🍏')
        st.markdown(f"<div style='background: #f4f4f7; border-radius: 10px; padding: 1.2em 0.5em; text-align: center; box-shadow: 0 2px 8px #eee;'><span style='font-size:2.2em;'>{emoji}</span><br><span style='font-size:1.3em; color:#222;'>Predicted Fruit:</span><br><b style='font-size:1.5em; color:#1a7f37;'>{pred_class}</b></div>", unsafe_allow_html=True)
    else:
        st.info("⬆️ Please upload a fruit image to get started.")
