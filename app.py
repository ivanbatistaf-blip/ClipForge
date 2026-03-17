import streamlit as st
import requests

st.set_page_config(page_title="ClipForge", layout="centered")

st.title("🎬 ClipForge - Gerador de Vídeos com IA")

roteiro = st.text_area("Digite seu roteiro:", height=200)

# Estado para manter o vídeo após clique
if "video_pronto" not in st.session_state:
    st.session_state.video_pronto = False

if st.button("Gerar vídeo"):
    if roteiro.strip() != "":
        st.session_state.video_pronto = True
    else:
        st.warning("Digite um roteiro!")

# Se já gerou vídeo, mostra tudo
if st.session_state.video_pronto:

    st.success("Vídeo gerado com sucesso!")

    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"

    st.video(video_url)

    try:
        response = requests.get(video_url)
        video_bytes = response.content

        st.download_button(
            label="📥 Baixar vídeo",
            data=video_bytes,
            file_name="clipforge_video.mp4",
            mime="video/mp4"
        )
    except:
        st.error("Erro ao carregar vídeo.")
