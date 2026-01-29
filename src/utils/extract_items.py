import re

# Extract items and their prices from receipt text
def extract_items_prices(text: str)-> list[dict] | None:
    items = []
    pending_item = None
    lines = text.splitlines()

    for line in lines:
        sl_pattern = r'^\d+\s+([A-Z][A-Z\s]+?)\s+(?:\d+\.\d{2}\s+)*(\d+\.\d{2})\s*.*$'
        
        # Process single-line items (ITEM 0.00)
        sl_item = re.match(sl_pattern, line)
        if sl_item:
            items.append({
                "item": sl_item.group(1),
                "price": float(sl_item.group(2))
            })
            pending_item = None
            continue
        
        # Process double-line items (ITEM\n QTY AT PRICE FOR TOTAL)
        dl_item_pattern = r'^\d+\s+([A-Z][A-Z\s]+)$'
        dl_item = re.match(dl_item_pattern, line)

        # Item name only line
        if dl_item:
            pending_item = dl_item.group(1)
            continue
        
        # Pricing line for previous item
        if pending_item:
            dl_prices_pattern = r'^(\d+)\s+AT\s+\d+\s+FOR\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s*.*$'
            
            dl_price = re.match(dl_prices_pattern, line)
            if dl_price:
                items.append({
                    "item": pending_item,
                    "quantity": int(dl_price.group(1)),
                    "unit_price" : float(dl_price.group(2)),
                    "total_price": float(dl_price.group(3))
                })
                pending_item = None

    return items or None


# Extract subtotal from receipt text
def extract_subtotal(text: str)->float | None:
    pattern = r'SUBTOTAL\s+(\d+\.\d{2})'
    
    subtotal = re.search(pattern, text)
    return float(subtotal.group(1)) if subtotal else None


# Extract taxes from receipt text
def extract_tax(text: str)-> list[dict] | None:
    tax = []
    pattern = r'TAX\s+(\d+)\s+(\d+)%\s+(\d+\.\d{2})'

    taxes = re.findall(pattern, text)

    for t in taxes:
        tax.append({
            "tax_number": int(t[0]),
            "tax_rate": int(t[1]),
            "tax_amount": float(t[2])
        })

    return tax or None


# Extract total from receipt text
def extract_total(text: str)-> float | None:
    pattern = r'\bTOTAL\b\s+(\d+\.\d{2})'

    total = re.search(pattern, text)
    return float(total.group(1)) if total else None 


# Extract last 4 digits from receipt text
def extract_last_digits(text: str)-> str | None:
    pattern = r'(?:VISA|MASTERCARD)[^\d]*(\d{4})'

    last_digits = re.search(pattern, text)
    return last_digits.group(1) if last_digits else None



