from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import os

def transcribe_to_midi(audio_path, label):
    os.makedirs("midi", exist_ok=True)
    prediction = predict(audio_path, model_path=ICASSP_2022_MODEL_PATH)
    midi_path = os.path.join("midi", f"{label}.mid")
    prediction['midi'].write(midi_path)
    return midi_path
