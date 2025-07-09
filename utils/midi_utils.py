from miditoolkit import MidiFile

def merge_midi_files(midi_paths):
    output = MidiFile()
    for path in midi_paths:
        mf = MidiFile(path)
        output.instruments.extend(mf.instruments)

    output_path = "output/final_tab.mid"
    output.dump(output_path)
    return output_path
