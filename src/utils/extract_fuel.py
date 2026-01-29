import re

# Extracts pump number and fuel type from receipt text
def extract_pump_fuel(text: str)-> dict[int, str] | None:
    pattern = r'Pump#\s+(\d+)\s+([A-Z]+)'

    pump_fuel = re.search(pattern, text)
    return {
        "pump_number": int(pump_fuel.group(1)),
        "fuel_type": pump_fuel.group(2)
    } if pump_fuel else None


# Extracts gallons from receipt text
def extract_gallons(text: str)-> float | None:
    pattern = r'Gallons\s+(\d+\.\d{3})'

    gallons = re.search(pattern, text)
    return float(gallons.group(1)) if gallons else None


# Extracts price per gallon from receipt text
def extract_price_per_gallon(text: str)-> float | None:
    pattern = r'Price/Gal\s+\$(\d+\.\d{3})'

    price_per_gallon = re.search(pattern, text)
    return float(price_per_gallon.group(1)) if price_per_gallon else None


# Extracts total cost from receipt text
def extract_total_cost(text: str)-> float | None:
    pattern = r'Fuel Sale\s+\$(\d+\.\d+)'
    
    total_cost = re.search(pattern, text)
    return float(total_cost.group(1)) if total_cost else None
