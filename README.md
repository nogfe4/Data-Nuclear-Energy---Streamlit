# [PT]: 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange) 
![Streamlit](https://streamlit.io/)
![Status](https://img.shields.io/badge/Status-Concluído-green)

# Dashboard de Análise de Energia Nuclear 

# Author: @nogfe4

Este é um aplicativo web interativo construído com Streamlit para visualizar e analisar dados sobre a geração de energia nuclear em todo o mundo. Com ele podemos organizar os dados, fazer comparações e analisar geograficamente a evolução da Energia Nuclear do mundo 
 

## 🚀 Funcionalidades

O aplicativo é dividido em várias páginas, cada uma com uma finalidade específica:

*   **Dashboard Principal**: Uma visão geral dos dados de energia nuclear dos EUA (fonte: EIA), com filtros interativos.
*   **Análise por País**: Permite selecionar um país e visualizar seu histórico de geração de energia nuclear em um gráfico de linha.
*   **Comparador Anual**: Uma ferramenta para comparar os maiores produtores de energia nuclear em dois anos distintos.

---

## 📄 Páginas do Aplicativo

### 1. Dashboard da Energia Nuclear Mundial (`app.py`)

A página inicial foca nos dados da *U.S. Energy Information Administration (EIA)*.

*   **Filtro Interativo**: Um slider na barra lateral permite filtrar os dados com base na "Geração Líquida de Eletricidade Nuclear".
*   **Gráficos**:
    *   Um gráfico de barras mostrando a contagem de usinas operacionais.
    *   Um histograma da distribuição da geração líquida de eletricidade.

### 2. Produção por País (`Pages/information2.py`)

Esta página oferece uma análise detalhada por país.

*   **Seleção de País**: Um menu suspenso na barra lateral permite escolher um país específico.
*   **Métricas**: Exibe o ano de pico de geração e o valor correspondente para o país selecionado.
*   **Gráfico Histórico**: Um gráfico de linha mostra a evolução da geração de energia nuclear ao longo dos anos para o país selecionado.

### 3. Comparador Anual (`Pages/information3.py`)

Ferramenta poderosa para comparar o desempenho entre diferentes anos.

*   **Seleção de Anos**: Permite selecionar dois anos para comparação.
*   **Análise de Pico**: Identifica e exibe o país com a maior produção de energia nuclear para cada um dos anos selecionados.
*   **Gráfico Comparativo**: Um gráfico de barras compara visualmente a produção dos dois maiores produtores encontrados.

---

## 📊 Fontes de Dados

Este projeto utiliza os seguintes conjuntos de dados, localizados na pasta `datasets/`:

1.  `nuclear_energy_overview_eia.csv`: Dados gerais sobre a energia nuclear nos EUA.
2.  `world_nuclear_energy_generation.csv`: Dados históricos sobre a geração de energia nuclear por entidade (países e grupos). 
Kaggle: [Nuclear Power Data](https://www.kaggle.com/datasets/alistairking/nuclear-energy-datasets) 


---

## 💻 Tecnologias Utilizadas

*   **Python** [Download](https://www.python.org/)
*   **Streamlit**: Para a criação do aplicativo web. - [Info] (https://streamlit.io/)
*   **Pandas**: Para manipulação e análise dos dados. - [Info] (https://pandas.pydata.org/)
*   **Plotly Express**: Para a criação dos gráficos interativos.[Info] (https://plotly.com/python/plotly-express/)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

*   Python 3.8+
*   Git (opcional, para clonar o repositório)

### Instalação

1.  Clone este repositório (ou baixe os arquivos para uma pasta).
2.  Navegue até a pasta do projeto pelo terminal.
3.  Instale as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Aplicativo

Para iniciar o aplicativo, execute o seguinte comando no seu terminal:

```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no seu navegador padrão. 

# [EN]: 

# Nuclear Energy Analysis Dashboard


This is an interactive web application built with Streamlit to visualize and analyze data on nuclear power generation worldwide. It allows you to organize data, make comparisons, and geographically analyze the evolution of Nuclear Energy across the globe.

## 🚀 Features

The application is divided into several pages, each with a specific purpose:

*   **Main Dashboard**: An overview of US nuclear energy data (source: EIA), with interactive filters.
*   **Analysis by Country**: Allows you to select a country and view its history of nuclear power generation on a line chart.
*   **Annual Comparator**: A tool to compare the top producers of nuclear energy in two distinct years.

---

## 📄 Application Pages

### 1. World Nuclear Energy Dashboard (`app.py`)

The homepage focuses on data from the *U.S. Energy Information Administration (EIA)*.

*   **Interactive Filter**: A slider in the sidebar allows filtering data based on "Net Nuclear Electricity Generation".
*   **Charts**:
    *   A bar chart showing the count of operational plants.
    *   A histogram of the distribution of net electricity generation.

### 2. Production by Country (`Pages/information2.py`)

This page offers a detailed analysis by country.

*   **Country Selection**: A dropdown menu in the sidebar allows you to choose a specific country.
*   **Metrics**: Displays the peak generation year and the corresponding value for the selected country.
*   **Historical Chart**: A line chart shows the evolution of nuclear power generation over the years for the selected country.

### 3. Annual Comparator (`Pages/information3.py`)

A powerful tool for comparing performance between different years.

*   **Year Selection**: Allows you to select two years for comparison.
*   **Peak Analysis**: Identifies and displays the country with the highest nuclear energy production for each of the selected years.
*   **Comparative Chart**: A bar chart visually compares the production of the two top producers found.

---

## 📊 Data Sources

This project uses the following datasets, located in the `datasets/` folder:

1.  `nuclear_energy_overview_eia.csv`: General data on nuclear energy in the US.
2.  `world_nuclear_energy_generation.csv`: Historical data on nuclear power generation by entity (countries and groups).
    Kaggle: [Nuclear Power Data](https://www.kaggle.com/datasets/alistairking/nuclear-energy-datasets)

---

## 💻 Technologies Used

*   **Python** [Download](https://www.python.org/)
*   **Streamlit**: For creating the web application. - [Info](https://streamlit.io/)
*   **Pandas**: For data manipulation and analysis. - [Info](https://pandas.pydata.org/)
*   **Plotly Express**: For creating interactive charts. [Info](https://plotly.com/python/plotly-express/)

---

## 🚀 How to Run the Project

### Prerequisites

*   Python 3.8+
*   Git (optional, for cloning the repository)

### Installation

1.  Clone this repository (or download the files to a folder).
2.  Navigate to the project folder via the terminal.
3.  Install the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the application, run the following command in your terminal:

```bash
streamlit run app.py 
