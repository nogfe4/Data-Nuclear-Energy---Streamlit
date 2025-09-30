import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Dashboard da Energia Nuclear Mundial") 
st.subheader("Organizados por Ano, Parâmetros de Geração e Capacidade, Países e Continentes")
st.markdown("Utilize os filtros na barra lateral para explorar os dados de geração líquida de capacidade nuclear")

df_over = pd.read_csv("datasets/nuclear_energy_overview_eia.csv")
df_gen = pd.read_csv("datasets/world_nuclear_energy_generation.csv") 


ger_liqmin = df_over["Nuclear Electricity Net Generation"].min()
ger_liqmax = df_over["Nuclear Electricity Net Generation"].max()

ger_liq = st.sidebar.slider("Geração Líquida de Eletricidade Nuclear [MWh]", ger_liqmin, ger_liqmax, ger_liqmax)
df_filtrado = df_over[df_over["Nuclear Electricity Net Generation"] <= ger_liq] 
df_filtrado

fig = px.bar(df_filtrado["Nuclear Generating Units, Total Operable Units"].value_counts()) 
fig2 = px.histogram(df_filtrado["Nuclear Electricity Net Generation"])
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)