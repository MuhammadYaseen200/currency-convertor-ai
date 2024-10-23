import streamlit as st
from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Streamlit app layout
st.title('Currency Converter')

# Input fields
amount = st.number_input('Enter amount:', min_value=0.0, format='%f')
from_currency = st.selectbox('From Currency', ('USD', 'EUR', 'PKR', 'GBP', 'INR', 'JPY', 'AUD', 'CAD'))
to_currency = st.selectbox('To Currency', ('USD', 'EUR', 'PKR', 'GBP', 'INR', 'JPY', 'AUD', 'CAD'))

# Convert currency
if st.button('Convert'):
    if from_currency != to_currency:
        converted_amount = c.convert(from_currency, to_currency, amount)
        st.write(f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
    else:
        st.write('Choose different currencies to convert.')

# Streamlit command to run the app
# To run: streamlit run <filename.py>
