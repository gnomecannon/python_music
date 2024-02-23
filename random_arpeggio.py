from music21 import stream, note, tempo, meter, scale
import random

def generate_midi():
    # Create a new stream for the piece
    s = stream.Stream()

    # Set the meter (time signature) and tempo
    s.append(meter.TimeSignature('15/16'))
    s.append(tempo.MetronomeMark(number=105))

    # Define the A major scale
    a_major = scale.HarmonicMinorScale('D')

    # Parameters for the MIDI generation
    num_measures = 75
    notes_per_measure = 15  # 4 beats * 4 sixteenth notes, in 4/4 time
    total_notes = num_measures * notes_per_measure
    octave_range = [2, 3, 4, 5]  # 3 octaves: 4, 5, 6

    # Define a list of probabilities for a note to be replaced with a rest
    rest_probabilities = [0.05, 0.15, 0.20, 0.35]  # Different probabilities

    # Generate arpeggiated 16th notes with randomized intervals
    for _ in range(total_notes):
        # Randomly select a rest probability from the list
        rest_probability = random.choice(rest_probabilities)
        if random.random() < rest_probability:  # If random number is less than rest_probability, add a rest
            s.append(note.Rest(quarterLength=0.25))
        else:
            # Randomly select an octave within the specified range
            octave = random.choice(octave_range)
            # Randomly select a note within the scale
            pitch_index = random.randint(0, 6)  # 7 scale degrees (0-6)
            # Calculate the Music21 pitch object
            pitch = a_major.pitchFromDegree(pitch_index + 1)  # Music21 scale degrees are 1-indexed
            pitch.octave = octave
            # Create and add the note to the stream
            n = note.Note(pitch, quarterLength=0.25)  # Sixteenth note
            s.append(n)

    # Define the MIDI file path
    midi_file_path = "output_file.mid"
    # Export the stream to a MIDI file
    s.write('midi', fp=midi_file_path)

    return midi_file_path

# Call the function and print the path of the generated MIDI file
midi_file_path = generate_midi()
print(f"MIDI file generated at: {midi_file_path}")