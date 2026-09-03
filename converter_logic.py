import requests

def get_available_currencies():
    url = "https://api.frankfurter.app/currencies"
    response = requests.get(url)
    data = response.json()
    return list(data.keys())

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][to_currency]

