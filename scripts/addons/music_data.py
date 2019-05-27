import os
import sys
import bpy

from mathutils import Vector
from bpy.props import FloatVectorProperty

blend_dir = os.path.dirname(bpy.data.filepath)
modules = os.path.join(blend_dir, "scripts\\modules")
scripts = os.path.join(blend_dir, "scripts\\addons")
if modules not in sys.path:
    sys.path.insert(0, modules)
if scripts not in sys.path:
    sys.path.insert(0, scripts)

import mido
from mido import MidiFile

def getVertices(midiFilename):
    midoMidi = MidiFile(scripts + "\\" + midiFilename)
    bytes = []
    for i, track in enumerate(midoMidi.tracks):
        for msg in track:
            if msg.bytes() not in bytes and len(msg.bytes()) == 3:
                temp = msg.bytes()
                for c in range(len(temp)):
                    temp[c] /= midoMidi.length
                bytes.append(temp)
    verts = []
    for byte in bytes:
        #This is blender specific
        verts.append(Vector((byte[0], byte[1] , byte[2]))) 
    return [verts, [], []]

def getEdges(midiFilename):
    verts = getVertices(midiFilename)
    edges = []
    for i in range(len(verts[0])):
        if i+1 < len(verts[0]):
            edges.append([i, i+1])
    verts[1] = edges
    return verts

def getFaces(midiFilename):
    edges = getEdges(midiFilename)
    faces = []
    for i in range(len(edges[0])):
        if i+3 < len(edges[0]):
            faces.append([i, i+1, i+2, i+3])
    edges[2] = faces
    return edges