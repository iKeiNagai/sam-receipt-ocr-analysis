from pathlib import Path
from src.pipeline import *
from src.parsers import *
from src.parsers import *

# Mass process files OCR to JSOn
fuel_receipts = Path("xraw-data/fuel-receipts")
items_receipts = Path("xraw-data/items-receipts")

process_folder(FuelParser(), fuel_receipts)
process_folder(ItemsParser(), items_receipts)



# Process single file
"""
single_file = Path("xraw-data/fuel-receipts/01f.png")

process_file(FuelParser(), single_file)
"""