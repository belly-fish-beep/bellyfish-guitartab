import streamlit as st
from utils.youtube_downloader import download_youtube_audio
# from utils.transcription import transcribe_to_midi  # You can re-enable this later

st.title("🎸 AI Guitar Tab Maker (Lite)")
st.subheader("Paste a YouTube link to get started")

yt_link = st.text_input("Paste YouTube link here")

if yt_link:
    st.info("Downloading audio from YouTube...")
    file_path = download_youtube_audio(yt_link)
    st.success("Audio downloaded!")

    # Uncomment below when transcription is working
    # st.info("Transcribing audio to MIDI...")
    # midi_path = transcribe_to_midi(file_path, "song")
    # st.success("Transcription complete!")

    # with open(midi_path, "rb") as f:
    #     st.download_button("🎼 Download MIDI", f, "guitar_tab.mid", "audio/midi")

    st.warning("✅ Audio downloaded! MIDI transcription not enabled yet.")
