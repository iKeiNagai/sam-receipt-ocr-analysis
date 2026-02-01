import pytesseract
from PIL import Image
from pathlib import Path

# Perform OCR on image and return extracted text
def ocr_image(path: Path)-> str | None:

    text = pytesseract.image_to_string(
        Image.open(path),
        config='--psm 6' #single uniform block of text
    )

    return text or None