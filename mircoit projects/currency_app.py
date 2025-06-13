import streamlit as st

st.title("💱 Offline Currency Converter")

# Sample hardcoded exchange rates (1 unit of base currency = rate in target currency)
exchange_rates = {
    "USD": {"USD": 1, "INR": 83.1, "EUR": 0.92, "GBP": 0.79},
    "INR": {"USD": 0.012, "INR": 1, "EUR": 0.011, "GBP": 0.0095},
    "EUR": {"USD": 1.09, "INR": 90.2, "EUR": 1, "GBP": 0.86},
    "GBP": {"USD": 1.27, "INR": 105.3, "EUR": 1.17, "GBP": 1},
}

currencies = list(exchange_rates.keys())

from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

if st.button("Convert"):
    rate = exchange_rates[from_currency][to_currency]
    converted = amount * rate
    st.success(f"Exchange Rate: 1 {from_currency} = {rate} {to_currency}")
    st.write(f"Converted Amount: {converted:.2f} {to_currency}")
