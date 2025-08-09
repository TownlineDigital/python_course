import pytesseract
from PIL import Image

# Optional: point to tesseract executable if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image
image = Image.open("example.jpeg")

# Extract text from image
text = pytesseract.image_to_string(image)

print("Text found in image:")
print(text)
