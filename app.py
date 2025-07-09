import streamlit as st
import os
import shutil
from utils.transcription import transcribe_to_midi

st.title("🎸 AI Guitar Tab Maker (Lite)")
st.subheader("Upload an audio file (.mp3 or .wav)")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

if uploaded_file:
    st.info("Saving your file...")
    os.makedirs("audio", exist_ok=True)
    file_path = os.path.join("audio", uploaded_file.name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    st.success("File uploaded!")

    st.info("Transcribing audio to MIDI...")
    midi_path = transcribe_to_midi(file_path, "song")

    st.success("Transcription complete!")

    with open(midi_path, "rb") as f:
        st.download_button(
            label="🎼 Download MIDI File",
            data=f,
            file_name="guitar_tab.mid",
            mime="audio/midi"
        )
