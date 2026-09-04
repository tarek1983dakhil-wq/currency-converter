import streamlit as st
from converter_logic import get_available_currencies, convert_currency


# Arabic names for common currencies
arabic_currency_names = {
    "EUR": "اليورو",
    "USD": "الدولار الأمريكي",
    "EGP": "الجنيه المصري",
    "SYP": "الليرة السورية",
    "GBP": "الجنيه الإسترليني",
    "TRY": "الليرة التركية",
    "SAR": "الريال السعودي",
    "AED": "الدرهم الإماراتي",
    "QAR": "الريال القطري",
    "KWD": "الدينار الكويتي",
    "BHD": "الدينار البحريني",
    "OMR": "الريال العماني",
    "JOD": "الدينار الأردني",
    "IQD": "الدينار العراقي",
    "LBP": "الليرة اللبنانية",
    "MAD": "الدرهم المغربي",
    "DZD": "الدينار الجزائري",
    "TND": "الدينار التونسي",
    "LYD": "الدينار الليبي",
    "CHF": "الفرنك السويسري",
    "CAD": "الدولار الكندي",
    "AUD": "الدولار الأسترالي",
    "JPY": "الين الياباني",
    "CNY": "اليوان الصيني",
    "INR": "الروبية الهندية",
}


# Language selector
language = st.selectbox(
    "Sprache / اللغة",
    ["Deutsch", "العربية"]
)


@st.cache_data
def load_currencies():
    return get_available_currencies()


currencies = load_currencies()


def format_currency(code):
    if language == "العربية":
        arabic_name = arabic_currency_names.get(code)
        if arabic_name:
            return f"{code} — {arabic_name}"
    return code


if language == "العربية":
    st.title("محول العملات")
    st.markdown("محول عملات بسيط باستخدام أسعار الصرف الحالية.")

    amount = st.number_input(
        "المبلغ",
        min_value=0.0,
        value=100.0
    )

    from_currency = st.selectbox(
        "من",
        currencies,
        format_func=format_currency
    )

    to_currency = st.selectbox(
        "إلى",
        currencies,
        format_func=format_currency
    )

else:
    st.title("Währungsrechner")
    st.markdown(
        "Ein einfacher Währungsrechner mit aktuellen Wechselkursen."
    )

    amount = st.number_input(
        "Betrag",
        min_value=0.0,
        value=100.0
    )

    from_currency = st.selectbox(
        "Von",
        currencies
    )

    to_currency = st.selectbox(
        "Nach",
        currencies
    )


result = convert_currency(
    amount,
    from_currency,
    to_currency
)


if language == "العربية":
    from_name = arabic_currency_names.get(from_currency, from_currency)
    to_name = arabic_currency_names.get(to_currency, to_currency)

    st.success(
        f"{amount} {from_name} = {result:.2f} {to_name}"
    )
else:
    st.success(
        f"{amount} {from_currency} = {result:.2f} {to_currency}"
    )