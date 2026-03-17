import streamlit as st
import requests
from moviepy.editor import ImageClip, AudioFileClip
import tempfile

ELEVEN_API_KEY = st.secrets["ELEVEN_API_KEY"]

st.title("🎬 ClipForge IA - Gerador de Vídeo")

roteiro = st.text_area("Digite seu roteiro")

def gerar_audio(texto):
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": texto
    }

    response = requests.post(url, headers=headers, json=data)
    return response.content

def gerar_imagem():
    # imagem simples (pode trocar depois por IA real)
    return "https://picsum.photos/800/600"

if st.button("Gerar vídeo"):
    if roteiro:

        st.info("Gerando áudio...")
        audio_bytes = gerar_audio(roteiro)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            f.write(audio_bytes)
            audio_path = f.name

        st.info("Baixando imagem...")
        img_url = gerar_imagem()

        img_data = requests.get(img_url).content

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
            f.write(img_data)
            img_path = f.name

        st.info("Montando vídeo...")

        audio_clip = AudioFileClip(audio_path)
        video = ImageClip(img_path).set_duration(audio_clip.duration)
        video = video.set_audio(audio_clip)

        video_path = "video_final.mp4"
        video.write_videofile(video_path, fps=24)

        st.success("Vídeo pronto!")

        st.video(video_path)

        with open(video_path, "rb") as f:
            st.download_button(
                "📥 Baixar vídeo",
                data=f,
                file_name="video.mp4",
                mime="video/mp4"
            )

    else:
        st.warning("Digite um roteiro")
