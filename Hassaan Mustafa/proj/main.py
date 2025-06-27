import cv2
import pytesseract
from PIL import Image
import re
from datetime import datetime
import json
import pycountry

# Load and resize image
img = cv2.imread("passport.jpg")
img = cv2.resize(img, (800, int(img.shape[0] * (800 / img.shape[1]))))
cv2.imwrite("resized.jpg", img)

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Preprocess image
image = cv2.imread("resized.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (800, int(gray.shape[0] * (800 / gray.shape[1]))))
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imwrite("processed.jpg", gray)

# OCR
text = pytesseract.image_to_string(gray)

print("---- Extracted Text ----")
print(text)

# Extract ID Number
id_number_match = re.search(r'\d{5}-\d{7}-\d', text)
id_number = id_number_match.group() if id_number_match else "Not found"

# Extract Dates (support dd-mm-yyyy and dd MMM yyyy)
date_matches = re.findall(r'\d{2}[./-]\d{2}[./-]\d{4}', text)
date_matches += re.findall(r'\d{2}\s+[A-Z]{3,}\s+\d{4}', text.upper())
parsed_dates = []
for d in date_matches:
    try:
        d_clean = d.replace('/', '-').replace('.', '-')
        try:
            parsed_dates.append(datetime.strptime(d_clean, "%d-%m-%Y"))
        except:
            parsed_dates.append(datetime.strptime(d_clean.upper(), "%d %b %Y"))
    except:
        continue
parsed_dates.sort()

dob = parsed_dates[0].strftime("%d-%m-%Y") if len(parsed_dates) > 0 else "Not found"
issue = parsed_dates[1].strftime("%d-%m-%Y") if len(parsed_dates) > 1 else "Not found"
expiry = parsed_dates[2].strftime("%d-%m-%Y") if len(parsed_dates) > 2 else "Not found"

# Extract lines
lines = text.strip().splitlines()
lines = [line.strip() for line in lines if line.strip()]

# Name and Father's Name (for CNIC and passport formats)
person_name = "Not found"
father_name = "Not found"

for i, line in enumerate(lines):
    if "father" in line.lower():
        if i + 1 < len(lines):
            father_name = lines[i + 1]
        for j in range(i - 1, max(i - 7, -1), -1):
            name_candidate = lines[j]
            if len(name_candidate.split()) >= 2:
                cleaned = re.sub(r'^(mr\.?|mrs\.?|ms\.?|wry)\s+', '', name_candidate.strip(), flags=re.IGNORECASE)
                if re.match(r'^[A-Za-z]{2,}( [A-Za-z]{2,})+', cleaned):
                    person_name = cleaned
                    break
        break

# Passport-style name fallback
if person_name == "Not found":
    for line in lines:
        if re.match(r'^[A-Z\s]{5,}$', line.strip()) and "REPUBLIC" not in line and "PAKISTAN" not in line:
            person_name = line.strip().title()
            break

if person_name != "Not found":
    i = lines.index(person_name.upper()) if person_name.upper() in lines else -1
    if i >= 0 and i + 1 < len(lines):
        next_line = lines[i + 1].strip()
        if re.match(r'^[A-Z\s]{5,}$', next_line):
            father_name = next_line.title()

# Card Type classification
text_lower = text.lower()
card_type = "Unknown"
if any(word in text_lower for word in ["identity", "identy", "dentity", "id card", "cnic", "national"]):
    card_type = "idcard"
elif any(word in text_lower for word in ["license", "driving", "permit"]):
    card_type = "license"
elif any(word in text_lower for word in ["passport", "immigration", "visa", "mrz"]):
    card_type = "passport"

# Country detection
country_detected = "Unknown"
all_countries = [country.name.lower() for country in pycountry.countries]
for c in all_countries:
    if c in text_lower:
        country_detected = c.title()
        break

# Print Extracted Fields
print("\n---- Extracted Fields ----")
print("ID Number:", id_number)
print("Date of Birth:", dob)
print("Issue Date:", issue)
print("Expiry Date:", expiry)
print("Name:", person_name)
print("Father's Name:", father_name)
print("Card Type:", card_type)
print("Country:", country_detected)

# Save to JSON
def safe_filename(s):
    return re.sub(r'[^A-Za-z0-9_-]', '_', s.strip())

filename_name = safe_filename(person_name.replace(" ", "_"))
filename_id = safe_filename(id_number)
filename = f"{filename_name}_{filename_id}.json"

data = {
    "ID Number": id_number,
    "Date of Birth": dob,
    "Issue Date": issue,
    "Expiry Date": expiry,
    "Name": person_name,
    "Father's Name": father_name,
    "Card Type": card_type,
    "Country": country_detected
}

with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"\n✅ Data saved to: {filename}")
