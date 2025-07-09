import streamlit as st
from utils.youtube_downloader import download_youtube_audio

st.title("🎸 AI Guitar Tab Maker (Lite)")
st.subheader("Paste a YouTube link to get started")

yt_link = st.text_input("Paste YouTube link here")

if yt_link:
    st.info("Downloading audio from YouTube...")
    file_path = download_youtube_audio(yt_link)
    st.success("Audio downloaded!")

    st.warning("✅ Audio downloaded! MIDI transcription not enabled yet.")
