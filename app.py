import streamlit as st

st.set_page_config(page_title="ClipForge", layout="centered")

st.title("🎬 ClipForge - Gerador de Vídeos com IA")

st.write("Digite seu roteiro abaixo:")

roteiro = st.text_area("Roteiro", height=200)

if st.button("Gerar vídeo"):
    if roteiro:
        st.success("Roteiro recebido com sucesso!")

        st.write("📜 Prévia do roteiro:")
        st.write(roteiro)

        # Simulação de geração
        st.info("Gerando vídeo... (simulação)")

        # Aqui depois vamos integrar IA real
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")

        st.download_button(
            "📥 Baixar vídeo",
            data="video",
            file_name="video.mp4"
        )
    else:
        st.warning("Digite um roteiro primeiro!")
