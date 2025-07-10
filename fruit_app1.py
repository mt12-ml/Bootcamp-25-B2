import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import os

# === MUST BE FIRST Streamlit command ===
st.set_page_config(page_title="🍓 Fruit Classifier", layout="centered", page_icon="🍍")

# === CONFIG ===
MODEL_PATH = 'best_scratch.pt'
IMAGE_SIZE = 224
CLASS_NAMES = ['Apple', 'Banana', 'Grapes', 'Guava', 'Mango', 'Orange', 'Papaya', 'Pomegranate', 'Strawberry', 'Watermelon']

# === Device ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# === Transform ===
transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], 
                         [0.229, 0.224, 0.225])
])

# === Model ===
class FruitClassifier(nn.Module):
    def __init__(self, num_classes):
        super(FruitClassifier, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

# === Load model ===
@st.cache_resource
def load_model():
    model = FruitClassifier(num_classes=len(CLASS_NAMES))
    checkpoint = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(device)
    model.eval()
    return model

model = load_model()

# === Prediction Function ===
def predict(image: Image.Image):
    img = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
        return CLASS_NAMES[predicted.item()]

# === Streamlit UI ===
st.markdown(
    """
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton>button {
            background-color: #34a853;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 0.5rem 1rem;
        }
        .stButton>button:hover {
            background-color: #2c8e45;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍇 Fruit Classifier(Scratch)")
st.markdown("Upload a fruit image and let the model predict what it is!")

# === Sidebar ===
with st.sidebar:
    st.header("Upload Image 📤")
    uploaded_file = st.file_uploader("Choose a fruit image...", type=["jpg", "jpeg", "png"])

    st.markdown("---")
    st.subheader("Available Fruits 🍉")
    for fruit in CLASS_NAMES:
        st.markdown(f"✅ {fruit}")

# === Main Area ===
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Predict Fruit 🍎"):
        prediction = predict(image)
        st.success(f"✅ **Predicted Fruit:** {prediction}")
else:
    st.info("👈 Upload an image from the sidebar to get started.")
