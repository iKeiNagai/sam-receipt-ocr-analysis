from src.pipeline import ocr_image, save_json
from src.parsers import *
from pathlib import Path

# Process all files in folder and Save OCR to JSON
def process_folder(parser: object, folder: Path)-> None:

    if not folder.exists():
        raise FileNotFoundError(f"No such folder: {folder}")

    """
    - Perform OCR to extract text
    - Parse extracted text into structured data
    - Store extracted OCR text with preserved line breaks
    - Save structured data as JSON
    """
    for file in folder.glob("*.png"):
        text = ocr_image(file)
        data = parser.parse(text)
        data['raw_ocr'] = text.splitlines(True)
        save_json(data, file.stem)



# Process single file and Save OCR to JSON
# Testing purpose
def process_file(parser: object, file: Path)-> None:

    if not file.exists():
        raise FileNotFoundError(f"No such file: {file}")
    
    text = ocr_image(file)
    data = parser.parse(text)
    data['raw_ocr'] = text.splitlines(True) 
    save_json(data, file.stem)

