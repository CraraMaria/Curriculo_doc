import streamlit as st
import pandas as pd

st.set_page_config(
      page_title="Maria Clara Fontenele Silva", 
      page_icon= "🍓", layout="centered", 
      initial_sidebar_state="auto", 
      menu_items= { 
          'Get Help':'https://www.extremelycoolapp.com/help',
          'Report a bug': 'https://www.extremelycoolapp.com/bug',
          'About': "# This is a header. This is an *extremely* cool app!"
      }
    )

col1, col2 = st.columns([4,1])

with col1:
    st.title("Maria Clara Fontenele Silva")
    st.write("Estudante de Ciência da Computação. Forte interesse em Ciência de Dados e segurança digital. Possuo experiência em projetos acadêmicos e voluntários e busco oportunidade de estágio para aplicar e expandir conhecimentos")
    
    st.divider() 

    st.subheader(":blue[PROJETOS]")
    st.write("Projeto Currículo — _Projeto Pyhton_")
    st.caption("Objetivo de criar esse currículo em um site usando a biblioteca Streamlit do Pyhton.")
    st.write("Projeto Guia do Universitário — _Projeto Integrador_")
    st.caption("Objetivo de criar uma solução prática através de uma plataforma web para ajudar aos calouros a contratar monitores e dicas sobre a faculdade e estudos.")
    st.write("Projeto Metamorfo — _Projeto de Extensão_")
    st.caption("Objetivo de criar uma forma de abordar a segurança digital para pessoas leigas e como os deixar tranquilos em relação a tecnologia")
    

    st.divider()

    st.subheader(":blue[CERTIFICAÇÃO]")
    st.write("Curso Pleno de Língua Estrangeira Moderna Inglês")
    st.caption("CONCLUÍDO 2017")
    st.caption("CENTRO INTERESCOLAR DE LÍNGUAS DO GAMA")

    st.divider()

    st.subheader(":blue[FORMAÇÃO]")
    st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
    st.caption("Bacharelado em Ciência da Computação")
    st.caption("Quarto semestre")
    st.caption("formatura final do segundo semestre de 2026")
    st.write("Centro de Ensino Médio Setor Leste, Asa Sul, DF")
    st.caption("Ensino Médio 2018")
    


with col2:

    st.caption("\n")
    st.caption("\n")
    st.caption("Santa Maria, DF, 72594-235")
    st.caption("**+55 61 98160-7950**")
    st.caption("**fontenelesilvamariaclara@gmail.com**")
    st.caption("**maria.silva27@iesb.edu.br**")
    
    st.divider()

    st.write(":blue[COMPETÊNCIAS]")
    st.caption("Programação em C; Java; Python.")
    st.caption("Análise de Dados: Excel, Python(Pandas, NumPy), SQL.")
    st.caption("Desenvolvimento web HTML e CSS.")
    st.caption("Ferramentas IDE: Eclipse; Visual Studio Code.")
    st.caption("Gestão de projetos; Metodologias: Scrum, Kanban. Com Microsoft Project, Trello e Jira.")
    st.caption("")

    st.divider()

    st.write(":blue[PROJETOS VOLUNTÁRIOS]")
    st.caption("**Monitoria no departamento de matemática** em geometria analítica e lógica matemática.")
    st.caption("**Apoio na aplicação de provas**, auxílio na organização e aplicação de provas para os alunos do EAD")

    st.divider()

    st.write(":blue[IDIOMAS]")
    st.caption("Inglês avançado")




