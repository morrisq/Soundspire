import os
import sys
import bpy
blend_dir = os.path.dirname(bpy.data.filepath)
modules = os.path.join(blend_dir, "scripts\\modules")
scripts = os.path.join(blend_dir, "scripts\\addons")
if modules not in sys.path:
    sys.path.insert(0, modules)
if scripts not in sys.path:
    sys.path.insert(0, scripts)

import os
import mido
from mido import MidiFile

def getVertices(midiFilename):
    midoMidi = MidiFile(scripts + "\\" + midiFilename)
    print("File successfully read")
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        # print('Track {}: {}'.format(i, track.name))
        for msg in track:
            # print("Message: " + str(msg))
            # print("Bytes: " + str(msg.bytes()))
            if(len(msg.bytes()) == 3):
                bytes.append(msg.bytes())

    # print("----------------------------------------------")
    # print(midoMidi.length)
    print(bytes)
    return bytes

#getVertices("sample1.mid")