import streamlit as st
import sys
import os

# Adiciona o diretório atual ao sys.path para permitir importações locais
sys.path.append(os.path.dirname(__file__))

from previsor import prever_resultado

st.title("🔮 Robô Preditor de Futebol")

time_casa = st.text_input("Time da Casa")
time_fora = st.text_input("Time Visitante")

if st.button("Prever"):
    resultado = prever_resultado(time_casa, time_fora)
    st.success(f"Previsão: {resultado}")
