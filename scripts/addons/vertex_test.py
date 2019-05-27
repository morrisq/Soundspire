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

import mido
from mido import MidiFile

def testUnique():
    a = [[1,2,3], [4,5,6], [1,2,3]]

    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in a: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print(x)

def printData(midiFilename):
    midoMidi = MidiFile(os.getcwd() + "\\" + midiFilename)
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        #print('Track {}: {}'.format(i, track.name))
        for msg in track:
            #print("Message: " + str(msg))
            print("Bytes: " + str(msg.bytes()))
            if msg.bytes() not in bytes:
                temp = msg.bytes()
                # print(temp)
                for c in range(len(temp)):
                    temp[c] /= midoMidi.length
                bytes.append(temp)
    print("----------------------------------------------")
    #print(midoMidi.length)
    print(bytes)
    return bytes

def getVertices(midiFilename):
    midoMidi = MidiFile(os.getcwd() + "\\" + midiFilename)
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        for msg in track:
            if msg.bytes() not in bytes:
                temp = msg.bytes()
                for c in range(len(temp)):
                    temp[c] /= midoMidi.length
                bytes.append(temp)
    return bytes

def getEdges(midiFilename):
    vertices = getVertices(midiFilename)
    

# testUnique();
printData("sample1.mid")
getVertices("sample1.mid")
# printData("freesia.mid")
# printData("journey.mid")