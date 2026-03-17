import streamlit as st
import requests

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="ClipForge", layout="centered")

# TÍTULO
st.title("🎬 ClipForge - Gerador de Vídeos com IA")

# CAMPO DE ROTEIRO
roteiro = st.text_area("Digite seu roteiro:", height=200)

# BOTÃO
if st.button("Gerar vídeo"):
    if roteiro.strip() != "":
        
        st.success("Roteiro recebido com sucesso!")

        st.write("📜 Seu roteiro:")
        st.write(roteiro)

        # LINK DE VÍDEO DE TESTE
        video_url = "https://www.w3schools.com/html/mov_bbb.mp4"

        st.info("Gerando vídeo...")

        # MOSTRAR VÍDEO
        st.video(video_url)

        # BAIXAR VÍDEO
        try:
            video_bytes = requests.get(video_url).content

            st.download_button(
                label="📥 Baixar vídeo",
                data=video_bytes,
                file_name="clipforge_video.mp4",
                mime="video/mp4"
            )
        except:
            st.error("Erro ao carregar vídeo para download.")

    else:
        st.warning("Digite um roteiro antes de gerar o vídeo!")
