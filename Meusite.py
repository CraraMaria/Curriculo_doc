import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Maria Clara Fontenele Silva",
    page_icon="🍓",
    layout="centered",
    initial_sidebar_state="auto"
)

# Tabulação
tab1, tab2 = st.tabs(["Currículo", "Outros Conteúdos"])

with tab1:
    # Colunas dentro da aba 1
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("Maria Clara Fontenele Silva")
        st.write("Estudante de Ciência da Computação. Interesse em Ciência de Dados e Desenvolvimento Fullstack.")
        st.write("Experiência em projetos acadêmicos e voluntários e em busca de estágio para aplicar conhecimentos.")

        st.divider()
        st.subheader(":blue[PROJETOS]")
        st.write("**Projeto Currículo** — _Projeto Python_")
        st.caption("Criação deste currículo interativo usando Streamlit.")
        st.write("**Projeto Guia do Universitário** — _Projeto Integrador_")
        st.caption("Solução prática para calouros, com dicas sobre a faculdade e contratação de monitores.")
        st.write("**Projeto Metamorfo** — _Projeto de Extensão_")
        st.caption("Aprimoramento da segurança digital para leigos, com foco na tranquilidade ao usar tecnologia.")
        
        st.divider()
        st.subheader(":blue[CERTIFICAÇÃO]")
        st.write("Curso Pleno de Língua Estrangeira Moderna Inglês — **Concluído em 2017**")
        st.caption("Centro Interescolar de Línguas do GAMA")

        st.divider()
        st.subheader(":blue[FORMAÇÃO]")
        st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
        st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")
        st.write("Centro de Ensino Médio Setor Leste, Asa Sul, DF")
        st.caption("Ensino Médio - Concluído em 2018")

    with col2:
        st.caption("Santa Maria, DF, 72594-235")
        st.caption("**☎️ +55 61 98160-7950**")
        st.caption("**fontenelesilvamariaclara@gmail.com**")
        st.caption("**maria.silva27@iesb.edu.br**")
        
        st.divider()
        st.write(":blue[COMPETÊNCIAS]")
        st.caption("Programação: C, Java, Python.")
        st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
        st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
        st.caption("Ferramentas: Eclipse, Visual Studio Code, Spring Boot.")
        st.caption("Gestão de Projetos: Scrum, Kanban, Microsoft Project, Trello, Jira.")

        st.divider()
        st.write(":blue[PROJETOS VOLUNTÁRIOS]")
        st.caption("Monitoria em Geometria Analítica e Lógica Matemática.")
        st.caption("Apoio na organização e aplicação de provas para o EAD.")
        
        st.divider()
        st.write(":blue[IDIOMAS]")
        st.caption("Inglês avançado")

with tab2:
    # Conteúdo para a aba 2
    st.write("Conteúdo para a aba 2.")

