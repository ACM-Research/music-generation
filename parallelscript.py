from music21 import converter, instrument, note, chord, common
import glob
import concurrent.futures

count = 0
cpus = 3

def find(mfile):
    print("Checking", mfile)
    
    midi = converter.parse(mfile)
    notes_to_parse = None
    parts = instrument.partitionByInstrument(midi)
    
    for instr in parts:
        if instr.partName.lower().startswith("piano"): # avoid electric piano, etc
            # making sure the algorithm is counting
            return (True, mfile)
            
    return (False, mfile)

all_files = glob.glob("midi_files/*.mid")

#outputs = common.runParallel(files, parallelFunction=find, updateFunction=True)

# one worker per core
with concurrent.futures.ThreadPoolExecutor(max_workers=cpus) as executor:
    for ret in executor.map(find, all_files):
        if ret[0]:
            count += 1
            print(f"Found piano part in {ret[1][11:]} ({count} so far)") # #{count} 
    
# with causes join
print(f"Total count: {count}")


