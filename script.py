from music21 import converter, instrument, note, chord
import glob
count = 0

for file in glob.glob("/midi_files/*.mid"):
    midi = converter.parse(file)
    notes_to_parse = None
    parts = instrument.partitionByInstrument(midi)
    print(parts.partName())
    count+=1
    #if parts.

print(count)

