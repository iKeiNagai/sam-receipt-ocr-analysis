import re

# Extracts club manager's name from receipt text
def extract_manager(text: str)-> str | None:
   pattern = r'CLUB\s+MANAGER(?:[ ]+([A-Z]+))?'

   club_manager = re.search(pattern, text)
   return club_manager.group(1) if club_manager else None


# Extracts date and time from receipt text
def extract_timestamp(text: str)-> dict[str, str] | None:
   pattern = r'(\d{2}/\d{2}/\d{2})\s+(\d{2}:\d{2})'

   date = re.search(pattern, text)

   return {
         "date": date.group(1),
         "time": date.group(2)
         } if date else None


# Extracts location (city, state) from receipt text
def extract_location(text: str)-> str | None:
   pattern = r'[A-Z]+(?:[ ]+[A-Z]+)*,\s+[A-Z]{2}'

   location = re.search(pattern, text)
   return location.group(0) if location else None


# Extract payment method from receipt text
def extract_payment_method(text: str)-> dict[str, str] | None:
   pattern = r'(VISA|MASTERCARD)\s+(CREDIT|DEBIT)'
   
   payment_method = re.search(pattern, text)
   return {
         "card_type": payment_method.group(1),
         "payment_type": payment_method.group(2)
         } if payment_method else None