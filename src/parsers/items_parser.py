from src.utils import *

class ItemsParser:

    # Extract structured items-receipt data from OCR text
    def parse(self, ocr_text):
        return{
            "type" : "items",
            "club_manager" : extract_manager(ocr_text),
            "date_time" : extract_timestamp(ocr_text),
            "location" : extract_location(ocr_text),
            "items" : extract_items_prices(ocr_text),
            "subtotal" : extract_subtotal(ocr_text),
            "tax" : extract_tax(ocr_text),
            "total" : extract_total(ocr_text),
            "payment_method" : extract_payment_method(ocr_text),
            "last_digits" : extract_last_digits(ocr_text)
        }