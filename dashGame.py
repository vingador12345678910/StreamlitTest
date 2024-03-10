import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.header('Dashboard estudo de Games')
st.text("Veja alguns gráficos de estudo")
df = pd.read_csv("ign.csv")

op= st.sidebar.selectbox(
    "Selecione as opções para mostrar os graficos",
    ("Quantidade de jogos por Plataforma","Jogos Anos")
)


if op=="Quantidade de jogos por Plataforma":
# Gráfico de barras para contar a quantidade de jogos por plataforma
    st.header("Quantidade de jogos por Plataforma")
    platform_counts = df["platform"].value_counts()
    fig = px.bar(x=platform_counts.index, y=platform_counts.values, labels={'x':'Plataforma', 'y':'Quantidade de Jogos'}, color_discrete_sequence=['#DAA520'])
    st.plotly_chart(fig)

if op=="Jogos Anos":
    
    opcao=st.radio(
    "Escolha um genero",
    ("RPG","Action")
)
    
    if opcao=="RPG":
        df_rpg = df[df["genre"] == "RPG"]
        st.header("Evoluçao dos Games durante os anos por Genero")
        df_rpg_mean = df_rpg.groupby('release_year').mean().reset_index()

        fig=px.line(df_rpg_mean,x="release_year")
        st.plotly_chart(fig)
    
    if opcao=="Action":
        df_action = df[df["genre"] == "Action"]
        st.header("Evoluçao dos Games durante os anos por Genero")
        df_action_mean = df_action.groupby('release_year').mean().reset_index()

        fig=px.line(df_action,x="release_year")
        st.plotly_chart(fig)

