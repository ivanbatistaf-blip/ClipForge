import streamlit as st
import requests

API_KEY = "af71ddd70ccbed3d1155ddda8e7ffaa46f5694f81dcc2e66b34aba267cb10296"

st.title("🎬 ClipForge - IA de Vídeo")

roteiro = st.text_area("Digite seu roteiro")

def gerar_audio(texto):
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": texto,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=data)

    return response.content

if st.button("Gerar narração"):
    if roteiro:

        st.info("Gerando voz com IA...")

        audio = gerar_audio(roteiro)

        st.audio(audio)

        st.download_button(
            "📥 Baixar áudio",
            data=audio,
            file_name="narracao.mp3",
            mime="audio/mpeg"
        )

    else:
        st.warning("Digite um roteiro")
