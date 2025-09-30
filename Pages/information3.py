import streamlit as st 
import pandas as pd
import plotly.express as px

# Carrega os dados. Para páginas secundárias, é bom carregar apenas o que for usar.
df_gen = pd.read_csv("datasets/world_nuclear_energy_generation.csv")

# Lista de entidades a serem excluídas (grupos de países, continentes, etc.)
entities_to_exclude = [
    'World', 'G20 (Ember)', 'High-income countries', 'OECD (EI)', 
    'OECD (EM)', 'OECD (Ember)', 'OECD (EU)', 'Central America (EI)', 
    'Central America (EM)', 'Central America (Ember)', 'G7 (Ember)', 
    'Europe (Ember)', 'Europe', 'North America (Ember)', 'Asia', 'Western Africa (EI)', 'Asia (Ember)', 'Asia (EI)', 'Europe (EI)', 'North America (EI)', 'Non-OECD (EI)'
]
# Filtra o DataFrame para excluir as entidades da lista de uma só vez
df_gen = df_gen[~df_gen['Entity'].isin(entities_to_exclude)]


# --- Configuração da Página e Barra Lateral ---
st.set_page_config(layout="wide")
st.title("Comparador Anual de Geração Nuclear")

st.sidebar.header("Filtros de Comparação")

# Cria a lista de anos únicos e a ordena de forma decrescente para o seletor
years = sorted(df_gen['Year'].unique(), reverse=True)

# Cria o seletor na barra lateral para escolher dois anos
selected_years = st.sidebar.multiselect(
    "Selecione 2 anos para comparar", 
    years,   
    max_selections=2,
    default=[years[0], years[1]] if len(years) > 1 else [] # Define valores padrão
) 

# --- Lógica de Comparação ---

# Continua apenas se o usuário tiver selecionado exatamente 2 anos
if len(selected_years) == 2:
    col1, col2 = st.columns(2)
    comparison_data = []

    # Itera sobre os dois anos selecionados
    for i, year in enumerate(selected_years):
        # Filtra o DataFrame para o ano atual
        df_year = df_gen[df_gen['Year'] == year]
        
        # Encontra a linha (país) com a maior geração de energia naquele ano
        top_producer = df_year.loc[df_year['electricity_from_nuclear_twh'].idxmax()]
        
        # Seleciona a coluna correta para exibir (col1 ou col2)
        column = col1 if i == 0 else col2
        
        with column:
            st.subheader(f"🏆 Maior Produtor em {year}")
            st.metric(label=top_producer['Entity'], value=f"{top_producer['electricity_from_nuclear_twh']:.2f} TWh")
        
        comparison_data.append(top_producer)

    # Cria um DataFrame com os dados para o gráfico
    df_comparison = pd.DataFrame(comparison_data)

    # --- Visualização ---
    st.subheader("Comparação Visual")
    fig = px.bar(
        df_comparison, 
        x='Entity', 
        y='electricity_from_nuclear_twh', 
        color='Entity',
        text=df_comparison['electricity_from_nuclear_twh'].apply(lambda x: f'{x:.2f} TWh'),
        title=f"Comparação de Pico de Geração: {selected_years[0]} vs {selected_years[1]}"
    )
    fig.update_layout(showlegend=False) # Oculta a legenda, pois as cores já identificam
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Por favor, selecione exatamente 2 anos na barra lateral para iniciar a comparação.")
