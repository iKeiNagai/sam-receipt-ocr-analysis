from unittest.mock import patch
from src.parsers import *

class TestParsers:

    # Test FuelParser outputs are correctly structured
    def test_fuel_parser_parse(self):
        ocr_text = "EXTRACTORS_MOCKED"

        with patch("src.parsers.fuel_parser.extract_manager", return_value="JOHN"), \
             patch("src.parsers.fuel_parser.extract_timestamp", return_value={
                "date": "01/25/25",
                "time": "18:47"
             }), \
             patch("src.parsers.fuel_parser.extract_location", return_value="ATLANTA, GA"), \
             patch("src.parsers.fuel_parser.extract_pump_fuel", return_value={
                 "pump number": 1,
                 "fuel type": "UNLEAD"
             }), \
             patch("src.parsers.fuel_parser.extract_gallons", return_value=12.345), \
             patch("src.parsers.fuel_parser.extract_price_per_gallon", return_value=1.234), \
             patch("src.parsers.fuel_parser.extract_total_cost", return_value=12.34), \
             patch("src.parsers.fuel_parser.extract_payment_method", return_value={
                 "card_type": "MASTERCARD",
                 "payment_type": "DEBIT"
             }):
            
            parser = FuelParser()
            result = parser.parse(ocr_text)


        assert result == {
            "type": "fuel",
            "club_manager": "JOHN",
            "date_time": {
                "date": "01/25/25",
                "time": "18:47"
            },
            "location": "ATLANTA, GA",
            "pump_fuel": {
                "pump number": 1,
                "fuel type": "UNLEAD"
            },
            "gallons": 12.345,
            "price_per_gallon": 1.234,
            "total_cost": 12.34,
            "payment_method": {
                "card_type": "MASTERCARD",
                "payment_type": "DEBIT"
            }
        }

    # Test ItemsParser outputs are correctly structured
    def test_items_parser_parse(self):
        ocr_text = "EXTRACTORS_MOCKED"

        with patch("src.parsers.items_parser.extract_manager", return_value="JOHN"), \
             patch("src.parsers.items_parser.extract_timestamp", return_value={
                "date": "01/25/25",
                "time": "18:47"
             }), \
             patch("src.parsers.items_parser.extract_location", return_value="ATLANTA, GA"), \
             patch("src.parsers.items_parser.extract_items_prices", return_value=[
                {
                    "item": "mockedItem",
                    "price": 12.34
                },
                {
                    "item": "DL Item",
                    "quantity": 1,
                    "unit price": 1.23,
                    "total price": 12.34
                }
             ]), \
             patch("src.parsers.items_parser.extract_subtotal", return_value=12.34), \
             patch("src.parsers.items_parser.extract_tax", return_value=[
                 {
                     "tax_number": 1,
                     "tax_rate": 2,
                     "tax_amount": 1.23
                 }
             ]), \
             patch("src.parsers.items_parser.extract_total", return_value=12.34), \
             patch("src.parsers.items_parser.extract_payment_method", return_value={
                 "card_type": "VISA",
                 "payment_type": "DEBIT"
             }), \
             patch("src.parsers.items_parser.extract_last_digits", return_value="1234"):

                parser = ItemsParser()
                result = parser.parse(ocr_text)

        assert result == {
            "type": "items",
            "club_manager": "JOHN",
            "date_time": {
                "date": "01/25/25",
                "time": "18:47"
            },
            "location": "ATLANTA, GA",
            "items": [
                {
                    "item": "mockedItem",
                    "price": 12.34
                },
                {
                    "item": "DL Item",
                    "quantity": 1,
                    "unit price": 1.23,
                    "total price": 12.34
                }
            ],
            "subtotal": 12.34,
            "tax": [
                {
                    "tax_number": 1,
                    "tax_rate": 2,
                    "tax_amount": 1.23
                }
            ],
            "total": 12.34,
            "payment_method": {
                "card_type": "VISA",
                "payment_type": "DEBIT"
            },
            "last_digits": "1234"
        }