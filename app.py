import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 
model = genai.GenerativeModel("gemini-2.0-flash")


st.set_page_config(page_title="Gerador de Receitas")
st.title("Gerador de Receitas Culinárias Personalizadas com IA")

ingredientes = st.text_area("Digite os Ingredientes Principais:")

culinaria = st.selectbox("Digite o tipo de culinária:", ["Italiana","Brasileira","Asiática","Mexicana","Qualquer uma"])

nivel = st.slider("Nível de Dificuldade (1 é Muito facil e 5 é Desafiador):",1,5)

restricao_chekbox = st.checkbox("Restrição Alimentar, se possuir marcar ")
restricao_texto = ""
if restricao_chekbox:
    restricao_alimentar = st.text_input("ex: sem glúten,vegetariana,sem lactose")


def logica(ingredientes,culinaria,nivel,restricao):
    prompt = (
        f"Sugira uma receita {culinaria} com nível de dificuldade {nivel} (1=muito fácil, 5=desafiador). "
        f"Use principalmente os seguintes ingredientes: {ingredientes}. "
        f"{'Considere a seguinte restrição alimentar: ' + restricao + '.' if restricao else ''} "
        f"Apresente o nome da receita, uma lista de ingredientes adicionais, e um breve passo a passo."
    )
    return prompt

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


if st.button("Sugerir Receita"):
    prompt = logica(ingredientes, culinaria, nivel, restricao_texto)
    with st.spinner("Gerando resposta ..."):
        resposta = gerar_resposta_gemini(prompt)
        st.write("**Resposta**")
        st.write(resposta)
   