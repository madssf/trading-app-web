import streamlit as st
import backend

market_data = backend.get_market_data()
#portfolio = backend.get_portfolios(backend.get_token())
st.header(f'Portfolio')
st.write(backend.get_req(backend.get_token(), 'bot/portfolios'))
