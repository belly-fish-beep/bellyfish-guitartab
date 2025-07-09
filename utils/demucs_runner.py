import os
import subprocess

def separate_stems(audio_path):
    output_dir = "stems/"
    os.makedirs(output_dir, exist_ok=True)

    # Run Demucs using command line
    # Assumes Demucs is installed and in PATH
    subprocess.run(["demucs", "-o", output_dir, audio_path], check=True)

    song_name = os.path.splitext(os.path.basename(audio_path))[0]
    stem_folder = os.path.join(output_dir, "htdemucs", song_name)

    stems = {
        "guitar": os.path.join(stem_folder, "other.wav"),
        "bass": os.path.join(stem_folder, "bass.wav"),
        "drums": os.path.join(stem_folder, "drums.wav"),
        "vocals": os.path.join(stem_folder, "vocals.wav"),
    }
    return stems
