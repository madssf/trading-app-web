import streamlit as st
import backend

market_data = backend.get_market_data()
data = backend.get_portfolios(backend.get_token())
st.write(data)
