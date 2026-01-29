from src.utils import *

class FuelParser:

    # Extract structured fuel-receipt data from OCR text
    def parse(self, ocr_text: str)-> dict:
        return {
            "type" : "fuel",
            "club_manager" : extract_manager(ocr_text),
            "timestamp" : extract_timestamp(ocr_text),
            "location" : extract_location(ocr_text),
            "pump_info" : extract_pump_fuel(ocr_text),
            "gallons" : extract_gallons(ocr_text),
            "price_per_gallon" : extract_price_per_gallon(ocr_text),
            "total_cost" : extract_total_cost(ocr_text),
            "payment_method" : extract_payment_method(ocr_text)
        }