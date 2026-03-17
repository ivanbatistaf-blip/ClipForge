import streamlit as st

st.title("🎬 ClipForge")

roteiro = st.text_area("Digite seu roteiro")

if st.button("Gerar vídeo"):
    if roteiro:

        st.success("Gerando vídeo...")

        # Simula imagem gerada
        st.image("https://picsum.photos/800/400")

        # Simula áudio narrado
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

        st.info("Vídeo sendo preparado... (próximo passo: geração real)")
    else:
        st.warning("Digite um roteiro")
