import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="sua chave aqui") # Coloca sua Api aqui


st.write("# Chatbot com IA") 

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = [] # Para guardar o histórico de mensagens do chat

texto_usuario = st.chat_input("Digite sua mensagem: ") # Input
arquivo_usuario = st.file_uploader("Envie um arquivo: ")


for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message('User').write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario} # Aqui vc vai criar a mensagem do usuário, para enviar para a IA
    st.session_state['lista_mensagens'].append(mensagem_usuario) # Aqui vc vai guardar a mensagem do usuário no histórico de mensagens do chat

#Ia resposta do chatbot
    resposta_ia = modelo_ia.chat.completions.create(
        messages = st.session_state['lista_mensagens'], # Aqui vc vai enviar o histórico de mensagens do chat para a IA
        model = 'gpt-4o'
    )
    print(resposta_ia.choices[0].message.content) # Aqui vc vai imprimir a resposta da IA
    texto_resposta_ia = resposta_ia.choices[0].message.content # Aqui vc vai colocar a resposta da IA

    st.chat_message('Assistant').write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia} # Aqui vc vai criar a mensagem da IA, para enviar para o histórico de mensagens do chat
    st.session_state['lista_mensagens'].append(mensagem_ia) # Aqui vc vai guardar a resposta da IA no histórico de mensagens do chat


print(st.session_state['lista_mensagens']) # Aqui vc vai ver o histórico de mensagens do chat, para verificar se está funcionando
