from src.utils import *

# Tests for extract_manager function
class TestExtractManager:
    def test_manager_present(self):
        text = "SAM'S CLUB\nCLUB MANAGER JOHNDOE\nATLANTA, GA\n"
        assert extract_manager(text) == "JOHNDOE"

    def test_no_club_manager(self):
        text = "SAM'S CLUB\nCLUB MANAGER\nATLANTA,GA\n"
        assert extract_manager(text) is None

    def test_multiple_spaces(self):
        text = "SAM'S CLUB\nCLUB  MANAGER  JOHNDOE\nATLANTA, GA\n"
        assert extract_manager(text) == "JOHNDOE"

# Tests for extract_timestamp function
class TestExtractTimestamp:
    def test_timestamp_present(self):
        text = "ATLANTA, GA\n01/17/25 18:30 1913 66643 90\n"
        assert extract_timestamp(text) ==  {"date": "01/17/25", "time": "18:30"}

    def test_no_timestamp(self):
        text = "ATLANTA, GA\nNo timestamp 0102\n"
        assert extract_timestamp(text) is None

class TestExtractLocation:
    def test_location_present(self):
        text = "SAM'S CLUB\nCLUB MANAGER\nATLANTA, GA\n"
        assert extract_location(text) == "ATLANTA, GA"

    def test_no_location(self):
        text = "SAM'S CLUB\nCLUB MANAGER\nNO LOCATION\n"
        assert extract_location(text) == None

    def test_different_location(self):
        text = "SAM'S CLUB\nCLUB MANAGER\n NEW YORK CITY, NY\n"
        assert extract_location(text) == "NEW YORK CITY, NY"

# Tests for extract_payment_method function
class TestExtractPaymentMethod:
    def test_payment_method_present(self):
        text = "Total 48.49\nVISA CREDIT\n"
        assert extract_payment_method(text) == {"card_type": "VISA", "payment_type": "CREDIT"}

    def test_no_payment_method(self):
        text = "Total 48.49\nCASH\n"
        assert extract_payment_method(text) is None

    def test_different_payment_method(self):
        text = "Total 48.49\nMASTERCARD DEBIT\n"
        assert extract_payment_method(text) == {"card_type": "MASTERCARD", "payment_type": "DEBIT"}

    def test_payment_method_with_extra_spaces(self):
        text = "Total 48.49\n  MASTERCARD   DEBIT \n"
        assert extract_payment_method(text) == {"card_type": "MASTERCARD", "payment_type": "DEBIT"}