from src.utils import *

# Tests for extract_fuel_pump function
class TestExtractPumpFuel:
    def test_pump_fuel_present(self):
        text = "Pump# 5 UNLEAD\nGallons 10.077"
        assert extract_pump_fuel(text) == {"pump_number": 5, "fuel_type": "UNLEAD"}

    def test_no_pump_fuel(self):
        text = "Pump# \nGallons 10.077"
        assert extract_pump_fuel(text) is None


# Tests for extract_gallons function
class TestExtractGallons:
    def test_gallons_present(self):
        text = "Pump# 5 UNLEAD\nGallons 10.077"
        assert extract_gallons(text) == 10.077

    def test_no_gallons(self):
        text = "Pump# 5 UNLEAD\nGallons"
        assert extract_gallons(text) is None


# Tests for extract_price_per_gallon function
class TestExtractPricePerGallon:
    def test_price_per_gallon_present(self):
        text = "Price/Gal $2.939\nFuel Sale $29.62"
        assert extract_price_per_gallon(text) == 2.939

    def test_no_price_per_gallon(self):
        text = "Price/Gal \nFuel Sale $29.62"
        assert extract_price_per_gallon(text) is None


# Tests for extract_total_cost function
class TestExtractTotalCost:
    def test_total_cost_present(self):
        text = "Price/Gal \nFuel Sale $29.62\nThanks"
        assert extract_total_cost(text) == 29.62

    def test_no_total_cost(self):
        text = "Price/Gal \nFuel Sale \nThanks"
        assert extract_total_cost(text) is None