import requests


def get_available_currencies():
    url = "https://api.frankfurter.dev/v2/currencies"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    currencies = [currency["iso_code"] for currency in data]

    return sorted(currencies)


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    rate = data["rate"]

    return amount * rate

