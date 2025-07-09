import streamlit as st
from utils.youtube_downloader import download_youtube_audio
from utils.demucs_runner import separate_stems
from utils.transcription import transcribe_to_midi
from utils.midi_utils import merge_midi_files
import os

st.title("🎸 AI Guitar Tab Maker")
st.subheader("Upload audio or paste a YouTube link")

input_method = st.radio("Select input method:", ["Upload audio file", "YouTube link"])

if input_method == "Upload audio file":
    uploaded = st.file_uploader("Upload song", type=["mp3", "wav"])
    if uploaded:
        os.makedirs("audio", exist_ok=True)
        file_path = f"audio/{uploaded.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded.read())

elif input_method == "YouTube link":
    yt_link = st.text_input("Paste YouTube link here")
    if yt_link:
        st.info("Downloading audio from YouTube...")
        os.makedirs("audio", exist_ok=True)
        file_path = download_youtube_audio(yt_link)
        st.success("Download complete!")

if 'file_path' in locals():
    st.info("Running stem separation (this may take a minute)...")
    stems = separate_stems(file_path)
    st.success("Stem separation complete!")

    st.info("Transcribing stems to MIDI...")
    midi_paths = []
    for part, stem_path in stems.items():
        midi_paths.append(transcribe_to_midi(stem_path, part))
    st.success("Transcription complete!")

    st.info("Merging MIDI files...")
    final_tab = merge_midi_files(midi_paths)
    st.success("MIDI files merged!")

    with open(final_tab, "rb") as f:
        st.download_button(
            "🎼 Download Guitar Pro Compatible MIDI",
            f,
            "my_tab.mid",
            "audio/midi",
        )
