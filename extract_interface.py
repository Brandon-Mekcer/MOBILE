import re

def extract_id(text):
    pattern = r"([A-Z0-9]+)\s*Confirmed"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

def extract_amount(text):
    pattern = r"Ksh\s*([\d,]+\.\d+)"
    match = re.search(pattern, text)
    if match:
        return float(match.group(1).replace(',', ''))
    return None

def extract_hour(text):
    pattern = r"(\d{1,2}):\d{2}"
    match = re.search(pattern, text)
    if match:
        return float(match.group(1))
    return None

def parse_sms(text):
    transaction_id = extract_id(text)
    amount = extract_amount(text)
    hour = extract_hour(text)
    return transaction_id, amount, hour

sms = "UGD6J903HS Confirmed. Ksh100.00 sent to Kevin Ombati on 7/5/2026 at 12:30 PM. New MPESA balance is Ksh1,500.70. Transaction cost, Ksh7.00."
# transaction_id = extract_id(sms)
# print("Extracted Transaction ID:", transaction_id)

# amount = extract_amount(sms)
# print("Extracted Amount:", amount)

# hour = extract_hour(sms)
# print("Extracted Hour:", hour)

transaction_id, amount, hour = parse_sms(sms)
print("Parsed SMS:")
print("Transaction ID:", transaction_id)
print("Amount:", amount)
print("Hour:", hour)
