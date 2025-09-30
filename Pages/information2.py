import streamlit as st 
import pandas as pd
import plotly.express as px

# Carrega os dados. Para páginas secundárias, é bom carregar apenas o que for usar.
df_gen = pd.read_csv("datasets/world_nuclear_energy_generation.csv")

# Cria a lista de países únicos para o seletor
countrys = df_gen['Entity'].unique()

# Cria o seletor na barra lateral para escolher um país
country = st.sidebar.selectbox("Selecione um País", countrys) 

# Filtra o DataFrame para conter apenas os dados do país selecionado
df_country = df_gen[df_gen['Entity'] == country]

# --- Exibição dos Detalhes (equivalente aos detalhes do livro) ---
st.title("Produção de Energia Nuclear por País")
st.subheader(country, divider="gray")

# Encontra o ano de maior geração e o valor correspondente
max_gen_row = df_country.loc[df_country['electricity_from_nuclear_twh'].idxmax()]
max_year = int(max_gen_row['Year'])
max_generation = max_gen_row['electricity_from_nuclear_twh']

st.write(f"**Pico de Geração:** O ano de maior geração de energia nuclear foi **{max_year}**.")
st.write(f"**Valor:** {max_generation:.2f} TWh")

# --- Exibição do Histórico (equivalente às avaliações) ---
st.subheader("Histórico de Geração de Energia Nuclear (TWh)")
fig = px.line(df_country, x="Year", y="electricity_from_nuclear_twh", title=f"Geração em {country}")
st.plotly_chart(fig, use_container_width=True)
