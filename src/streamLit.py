import streamlit as st

st.title(" Aprendendo Streamlit")
if "contador_doacoes" not in st.session_state:
    # Se a chave 'contador_doacoes' ainda não existir na memória da sessão atual do usuário, nós a criamos e a inicializamos com o valor 0.
    st.session_state.contador_doacoes = 0

    col1, col2 = st.columns(2)

    # 'st.button()' desenha o botão na tela e retorna True APENAS no momento em que é clicado.
    if st.button("Registrar Doação (+10 kg)"):
        # Se o usuário clicar neste botão, adicionamos +10 ao valor que já está guardado no session_state.
        st.session_state.contador_doacoes += 10

        with col2:
    # Desenha o segundo botão na tela.
            if st.button("Zerar Painel"):
        # Se o usuário clicar neste botão, redefinimos o contador guardado diretamente para 0.
                st.session_state.contador_doacoes = 0
                st.metric(
                label="Total de Alimentos no Dia", 
                value=f"{st.session_state.contador_doacoes} kg"
                )