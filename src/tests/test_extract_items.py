from src.utils import *

# Test for extract_items_prices function
class TestExtractItemsPrices:
    def test_items_prices_present(self):
        text = "00001 APPLES 10.00 X\n00002 BANANAS\n2 AT 1 FOR 5.00 10.00 Y\n"
        assert extract_items_prices(text) == [
            {"item": "APPLES", "price": 10.00},
            {"item": "BANANAS", "quantity": 2, "unit_price": 5.00, "total_price": 10.00}
        ]

    def test_no_items_prices(self):
        text = "00001 \n00002 \n"
        assert extract_items_prices(text) is None

    def test_multiple_double_line_items(self):
        text ="00001 APPLES\n3 AT 1 FOR 2.00 6.00 X\n00002 BANANAS\n2 AT 1 FOR 5.00 10.00 Y\n"
        assert extract_items_prices(text) == [
            {"item": "APPLES", "quantity": 3, "unit_price": 2.00, "total_price": 6.00},
            {"item": "BANANAS", "quantity": 2, "unit_price": 5.00, "total_price": 10.00}
        ]


# Test for extract_subtotal function
class TestExtractSubtotal:
    def test_subtotal_present(self):
        text ="SUBTOTAL 46.83\nTAX 1\n"
        assert extract_subtotal(text) == 46.83
    
    def test_no_subtotal(self):
        text = "SUBTOTAL \nTAX 1\n"
        assert extract_subtotal(text) is None


# Test for extract_tax function
class TestExtractTax:
    def test_tax_present(self):
        text = "SUBTOTAL 46.83\nTAX 1 7% 0.40\nTAX 2 2% 1.26\n"
        assert extract_tax(text) == [
            {"tax_number": 1, "tax_rate": 7, "tax_amount": 0.40},
            {"tax_number": 2, "tax_rate": 2, "tax_amount": 1.26}
        ]
    
    def test_no_tax(self):
        text = "SUBTOTAL 46.83\nTAX \n"
        assert extract_tax(text) is None


# Test for extract_total function
class TestExtractTotal:
    def test_total_present(self):
        text = "SUBTOTAL 46.83\nTAX 1 7% 0.40\nTOTAL 48.49\n"
        assert extract_total(text) == 48.49

    def test_no_total(self):
        text = "SUBTOTAL 46.83\nTAX 1 7% 0.40\nTOTAL \n"
        assert extract_total(text) is None


# Test for extract_last_digits function
class TestExtractLastDigits:
    def test_last_digits_present(self):
        text = "VISA DEBIT TEND 48.49\nVISA *#** KHER HHER 9943\n"
        assert extract_last_digits(text) == "9943"

    def test_no_last_digits(self):
        text = "VISA DEBIT TEND 48.49\nVISA *#** KHER HHER asdr\n"
        assert extract_last_digits(text) is None