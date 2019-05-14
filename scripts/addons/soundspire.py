bl_info = {
    "name": "Soundvironment",
    "author": "Quinn Morris",
    "version": (0, 1),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Procedurally generates a mesh from a music file",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

'''
This is the main file that will be run by blender.
This will depend on the BLENDER version of python.
This will call on dependencies that WILL depend on the system python 
The dependencies will use the system python to create specifically generated output in the form of 
a text file full of vertices, edges and faces, etc...

So essentially, a text file will be the middleman
'''

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

import sys
import os

#This takes the current directory the blender file is in and
#makes sure the system path has access to the music file data.
blend_dir = os.path.dirname(bpy.data.filepath)
modules = os.path.join(blend_dir, "scripts\\modules")
scripts = os.path.join(blend_dir, "scripts\\addons")
if modules not in sys.path:
    sys.path.insert(0, modules)
if scripts not in sys.path:
    sys.path.insert(0, scripts)

#music_data is a custom module referencing all the functions in the music_data.py file
#importlib reloads the import so you can edit music_data or any other custom module
import music_data
import importlib
importlib.reload(music_data)

#This is just to differentiate between versions of the module.
test_num = 2

def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y
    
    bytes = music_data.getVertices("sample1.mid")
    verts = []
    for byte in bytes:
        verts.append(Vector((byte[0] * scale_x, byte[1] * scale_y, byte[2])))
    edges = []
    faces = []

    mesh = bpy.data.meshes.new(name="New Test Mesh " + str(test_num))
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    #mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)

class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale = FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):
        add_object(self, context)
        return {'FINISHED'}


# Registration
def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Soundspire " + str(test_num),
        icon='VIEW3D')


# This allows you to right click on a button and link to the manual
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/dev/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "editors/3dview/object"),
        )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()