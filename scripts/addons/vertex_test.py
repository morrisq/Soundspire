import os
'''
import sys
import bpy
blend_dir = os.path.dirname(bpy.data.filepath)
modules = os.path.join(blend_dir, "scripts\\modules")
scripts = os.path.join(blend_dir, "scripts\\addons")
if modules not in sys.path:
    sys.path.insert(0, modules)
if scripts not in sys.path:
    sys.path.insert(0, scripts)
'''

print(os.getcwd())

import mido
from mido import MidiFile

def printData(midiFilename):
    midoMidi = MidiFile(os.getcwd() + "\\" + midiFilename)
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print("Message: " + str(msg))
            print("Bytes: " + str(msg.bytes()))
            bytes.append(msg.bytes())
    print("----------------------------------------------")
    print(midoMidi.length)
    print(bytes)
    return bytes

def getVertices(midiFilename):
    midoMidi = MidiFile(os.getcwd() + "\\" + midiFilename)
    print("File successfully read: " + str(os.getcwd() + "\\" + midiFilename))
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        for msg in track:
            if(len(msg.bytes()) == 3):
                bytes.append(msg.bytes())
    return bytes

#printData("sample1.mid")
printData("freesia.mid")
#printData("journey.mid")