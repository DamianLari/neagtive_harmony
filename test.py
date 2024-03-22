import mido
from mido import MidiFile, MidiTrack, Message

def invert_midi(input_file, output_file, inversion_point=60):
    original_midi = MidiFile(input_file)
    inverted_midi = MidiFile()

    for track in original_midi.tracks:
        new_track = MidiTrack()
        inverted_midi.tracks.append(new_track)

        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                # Inverser la hauteur des notes
                msg.note = 2 * inversion_point - msg.note
            new_track.append(msg)

    inverted_midi.save(output_file)

# Exemple d'utilisation
input_file = 'test.mid'
output_file = 'inverted_song.mid'
invert_midi(input_file, output_file)
