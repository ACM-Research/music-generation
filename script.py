from music21 import converter, instrument, note, chord
import glob
count = 0

for file in glob.glob("midi_files/*.mid"):
    midi = converter.parse(file)
    notes_to_parse = None
    parts = instrument.partitionByInstrument(midi)
    for instr in parts:
        if instr.partName == "Piano":
            count += 1
            # making sure the algorithm is counting
            print(f"Found piano part #{count} in {file[11:]}")

print(f"Total count: {count}")
