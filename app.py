import streamlit as st
from converter_logic import get_available_currencies, convert_currency


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)


# --------------------------------------------------
# Arabic currency names
# --------------------------------------------------

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


# --------------------------------------------------
# Styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(circle at 15% 20%, rgba(20, 184, 166, 0.10), transparent 25%),
            radial-gradient(circle at 85% 15%, rgba(59, 130, 246, 0.10), transparent 25%),
            linear-gradient(
                135deg,
                #f0f9ff 0%,
                #f8fafc 45%,
                #ecfeff 100%
            );
    }

    .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .money-banner {
        text-align: center;
        font-size: 2rem;
        letter-spacing: 0.7rem;
        opacity: 0.75;
        margin-bottom: 0.5rem;
        animation: floatMoney 4s ease-in-out infinite;
    }

    @keyframes floatMoney {
        0% {
            transform: translateY(0px);
        }

        50% {
            transform: translateY(-5px);
        }

        100% {
            transform: translateY(0px);
        }
    }

    .main-card {
        background: rgba(255, 255, 255, 0.96);
        padding: 2.2rem;
        border-radius: 26px;
        box-shadow:
            0 18px 45px rgba(15, 23, 42, 0.10);
        border: 1px solid rgba(148, 163, 184, 0.18);
        margin-bottom: 1.5rem;
    }

    .hero-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: #0f766e;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1rem;
        color: #64748b;
        margin-bottom: 1.8rem;
    }

    div[data-baseweb="select"] > div {
        border-radius: 14px;
        border-color: #cbd5e1;
    }

    div[data-testid="stNumberInput"] input {
        border-radius: 14px;
    }

    div[data-testid="stSelectbox"] > div:hover {
        transform: translateY(-1px);
        transition: 0.2s ease;
    }

    .result-card {
        margin-top: 1.6rem;
        padding: 1.5rem;
        border-radius: 20px;
        background:
            linear-gradient(
                135deg,
                #ccfbf1,
                #dbeafe
            );
        box-shadow:
            0 10px 25px rgba(15, 118, 110, 0.12);
        text-align: center;
        font-size: 1.5rem;
        font-weight: 800;
        color: #0f172a;
        border: 1px solid rgba(20, 184, 166, 0.18);
    }

    .footer-note {
        text-align: center;
        color: #94a3b8;
        font-size: 0.82rem;
        margin-top: 1.3rem;
    }

    .developer-card {
        text-align: center;
        margin-top: 1.8rem;
        padding-top: 1.2rem;
        border-top: 1px solid #e2e8f0;
    }

    .developer-name {
        font-size: 1rem;
        font-weight: 700;
        color: #0f766e;
    }

    .developer-tech {
        font-size: 0.85rem;
        color: #64748b;
        margin-top: 0.25rem;
    }

    .developer-link {
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }

    .developer-link a {
        text-decoration: none;
        font-weight: 700;
        color: #2563eb;
    }

    .developer-link a:hover {
        text-decoration: underline;
    }

    @media (max-width: 600px) {

        .block-container {
            padding-top: 1rem;
        }

        .main-card {
            padding: 1.2rem;
            border-radius: 20px;
        }

        .hero-title {
            font-size: 2rem;
        }

        .money-banner {
            font-size: 1.5rem;
            letter-spacing: 0.3rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Load currencies
# --------------------------------------------------

@st.cache_data
def load_currencies():
    return get_available_currencies()


currencies = load_currencies()


# --------------------------------------------------
# Decorative currency symbols
# --------------------------------------------------

st.markdown(
    '<div class="money-banner">💶 💵 💷 💴 🪙</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Language selector
# --------------------------------------------------

language = st.selectbox(
    "Sprache / اللغة",
    ["Deutsch", "العربية"]
)


# --------------------------------------------------
# Currency display
# --------------------------------------------------

def format_currency(code):

    if language == "العربية":

        arabic_name = arabic_currency_names.get(code)

        if arabic_name:
            return f"{code} — {arabic_name}"

    return code


# --------------------------------------------------
# Language texts
# --------------------------------------------------

if language == "العربية":

    title = "💱 محول العملات"

    subtitle = "تحويل العملات باستخدام أسعار الصرف الحالية"

    amount_label = "المبلغ"

    from_label = "من"

    to_label = "إلى"

else:

    title = "💱 Währungsrechner"

    subtitle = "Währungen mit aktuellen Wechselkursen umrechnen"

    amount_label = "Betrag"

    from_label = "Von"

    to_label = "Nach"


# --------------------------------------------------
# Main card
# --------------------------------------------------

st.markdown(
    '<div class="main-card">',
    unsafe_allow_html=True
)


st.markdown(
    f'<div class="hero-title">{title}</div>',
    unsafe_allow_html=True
)


st.markdown(
    f'<div class="hero-subtitle">{subtitle}</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Amount
# --------------------------------------------------

amount = st.number_input(
    amount_label,
    min_value=0.0,
    value=100.0
)


# --------------------------------------------------
# Currency selection
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    from_currency = st.selectbox(
        from_label,
        currencies,
        format_func=format_currency
    )


with col2:

    to_currency = st.selectbox(
        to_label,
        currencies,
        format_func=format_currency
    )


# --------------------------------------------------
# Conversion
# --------------------------------------------------

result = convert_currency(
    amount,
    from_currency,
    to_currency
)


# --------------------------------------------------
# Result
# --------------------------------------------------

if language == "العربية":

    from_name = arabic_currency_names.get(
        from_currency,
        from_currency
    )

    to_name = arabic_currency_names.get(
        to_currency,
        to_currency
    )

    result_text = (
        f"{amount:.2f} {from_name} = "
        f"{result:.2f} {to_name}"
    )

else:

    result_text = (
        f"{amount:.2f} {from_currency} = "
        f"{result:.2f} {to_currency}"
    )


st.markdown(
    f'<div class="result-card">{result_text}</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# API note
# --------------------------------------------------

st.markdown(
    '<div class="footer-note">'
    'Live exchange rates powered by Frankfurter API'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Developer information
# --------------------------------------------------

st.markdown(
    '<div class="developer-card">'
    '<div class="developer-name">Developed by Tarek Aldakhil</div>'
    '<div class="developer-tech">Python • Streamlit • REST API</div>'
    '<div class="developer-link">'
    '<a href="https://github.com/tarek1983dakhil-wq" target="_blank">'
    'GitHub'
    '</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)