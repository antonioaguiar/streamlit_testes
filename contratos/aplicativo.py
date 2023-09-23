import streamlit as st
import pandas as pd
import numpy as np

# configurar a página 
st.set_page_config(page_title="Minha Home Page")

# Using "with" notation
with st.sidebar:
    # adicionar combo para selecionar período em qtde de dias
    #qtde_dias = st.selectbox("Selecione o período", [7,15,21,30,45,60])
    #add_radio = st.radio(
    #    "Choose a shipping method",
    #    ("Standard (5-15 days)", "Express (2-5 days)")
    #)
    options = st.multiselect(
        'Períodos',[7,15,21,30,45,60])
    
    options2 = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],)

    #st.write('You selected:', options)

    qtde_dias = st.slider('Período', 0, 7, 60)
    #st.write("I'm ", age, 'years old')

with st.container():
    # conteudo
    st.subheader("Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados")
    #st.write("Quer aprender python? [Clique aqui](https://www.python.org)")

# função para carregar os dados
# @st.cache_data - > decorator para adicionar funcionalidade de cache no navegador
@st.cache_data
def carregar_dados(dias):
     tabela = pd.read_csv("contratos.csv")
     tabela = tabela[-dias:]   
     return tabela

with st.container():

    # usar panda para carregar os contratos
    dados = carregar_dados(qtde_dias)
     # Dashboard de contratos
    st.write("---")  #separador <hr>

    #https://docs.streamlit.io/library/api-reference/charts/st.line_chart    
    #st.area_chart(dados, x='Data', y='Contratos')
    st.line_chart(dados, x='Data', y='Contratos')

 # Using object notation
#add_selectbox = st.sidebar.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone")
#)

with st.container():
    tab1, tab2 = st.tabs(["📈 Gráfico", "🗃 Dados"])
    data = carregar_dados(qtde_dias)

    tab1.subheader("Gráfico dos contratos")
    tab1.bar_chart(data, x='Data', y='Contratos')

    tab2.subheader("Contratos")
    tab2.write( data['Contratos'] )


 
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
