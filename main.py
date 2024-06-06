# app/main.py
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title('🦜🔗Physics_Tutor')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    prompt_template = PromptTemplate(
        input_variables = ['input'],
        template='''You are a 9th Grade AI Physics Tutor and your name is ATP, 
        I will be writing something about Physics and you have to tell me if I am right or wrong in two sentences.
        Here is my write-up. {input}'''     
    )

    prompt = prompt_template.format(input = input_text)

    st.info(llm.invoke(prompt))
    #return 

with st.form('my_form'):
    text = st.text_area('What doubts do you have?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
