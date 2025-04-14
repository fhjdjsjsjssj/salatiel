import streamlit as st
import pandas as pd

sheet_url = st.secrets["sheet_url"]

@st.cache_data
def carregar_dados(url):
    return pd.read_csv(url)

dados = carregar_dados(sheet_url)

st.title("📊 Meu Dashboard com Streamlit")
st.write("Aqui estão os dados da planilha:")
st.dataframe(dados)