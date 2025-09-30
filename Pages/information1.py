import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout="wide")
st.title('Dashboard da Energia Nuclear Mundial') 
st.subheader("Informações sobre o Projeto") 

st.markdown("")


multi = '''# Dashboard de Análise de Energia Nuclear 

# Author: 🐱 [@nogfe4](https://github.com/nogfe4) 

Este é um aplicativo web interativo construído com Streamlit para visualizar e analisar dados sobre a geração de energia nuclear em todo o mundo. Com ele podemos organizar os dados, fazer comparações e analisar geograficamente a evolução da Energia Nuclear do mundo 

# [Dataset](https://www.kaggle.com/datasets/alistairking/nuclear-energy-datasets)

## 🚀 Funcionalidades

O aplicativo é dividido em várias páginas, cada uma com uma finalidade específica:

*   **Dashboard Principal**: Uma visão geral dos dados de energia nuclear dos EUA (fonte: EIA), com filtros interativos.
*   **Análise por País**: Permite selecionar um país e visualizar seu histórico de geração de energia nuclear em um gráfico de linha.
*   **Comparador Anual**: Uma ferramenta para comparar os maiores produtores de energia nuclear em dois anos distintos.

---

## 📄 Páginas do Aplicativo

### 1. Dashboard da Energia Nuclear Mundial

A página inicial foca nos dados da *U.S. Energy Information Administration (EIA)*.

*   **Filtro Interativo**: Um slider na barra lateral permite filtrar os dados com base na "Geração Líquida de Eletricidade Nuclear".
*   **Gráficos**:
    *   Um gráfico de barras mostrando a contagem de usinas operacionais.
    *   Um histograma da distribuição da geração líquida de eletricidade.

### 2. Produção por País 

Esta página oferece uma análise detalhada por país.

*   **Seleção de País**: Um menu suspenso na barra lateral permite escolher um país específico.
*   **Métricas**: Exibe o ano de pico de geração e o valor correspondente para o país selecionado.
*   **Gráfico Histórico**: Um gráfico de linha mostra a evolução da geração de energia nuclear ao longo dos anos para o país selecionado.

### 3. Comparador Anual 

Ferramenta poderosa para comparar o desempenho entre diferentes anos.

*   **Seleção de Anos**: Permite selecionar dois anos para comparação.
*   **Análise de Pico**: Identifica e exibe o país com a maior produção de energia nuclear para cada um dos anos selecionados.
*   **Gráfico Comparativo**: Um gráfico de barras compara visualmente a produção dos dois maiores produtores encontrados.

---

## 📊 Fontes de Dados

Este projeto utiliza os seguintes conjuntos de dados, localizados no dataset: [Nuclear Power Data](https://www.kaggle.com/datasets/danielleyank/eia-nuclear-power-plant-data) 

---

## 💻 Tecnologias Utilizadas

*   **Python** [Download](https://www.python.org/)
*   **Streamlit**: Para a criação do aplicativo web. - [Info](https://streamlit.io/)
*   **Pandas**: Para manipulação e análise dos dados. - [Info](https://pandas.pydata.org/)
*   **Plotly Express**: Para a criação dos gráficos interativos.[Info](https://plotly.com/python/plotly-express/)


'''
st.markdown(multi)