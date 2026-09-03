import streamlit as st
from converter_logic import get_available_currencies, convert_currency

st.title("Währungsrechner")
st.markdown("Ein einfacher Währungsrechner mit aktuellen Wechselkursen.")
amount = st.number_input("Betrag", min_value=0.0, value=100.0)
@st.cache_data
def load_currencies():
        return get_available_currencies()
currencies = load_currencies()
from_currency = st.selectbox("Von", currencies)
to_currency = st.selectbox("Nach", currencies)
result = convert_currency(amount, from_currency, to_currency)
st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
