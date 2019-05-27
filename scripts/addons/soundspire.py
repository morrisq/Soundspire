bl_info = {
	"name": "Soundspire",
	"author": "Quinn Morris",
	"version": (0, 1),
	"blender": (2, 75, 0),
	"location": "View3D > Add > Mesh > New Object",
	"description": "Generates a mesh based on data from a music file",
	"warning": "",
	"wiki_url": "",
	"category": "Add Mesh",
}

'''
As of right now, this works with Blender 2.79b and relies on Python 3.5.3(?) in order to work
You will need to install the python library "mido" using pip. Instructions are
available on the mido documentation page or github https://github.com/mido/mido
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
#soundviron.py needs to be used in blender tho.
#importlib reloads the import so you can edit music_data or any other custom module
import music_data
import importlib
importlib.reload(music_data)

#This is just to differentiate between versions of the module, can be an int or string.
test_id = "3"

def get_data(num, name):
	if num == 1:
		return music_data.getVertices(name)
	elif num == 2:
		return music_data.getEdges(name)
	elif num == 3:
		return music_data.getFaces(name)
	else:
		return [[], [], []]

def add_object(self, context):
	scale_x = self.scale.x
	scale_y = self.scale.y
	
	#Name of the midi file.
	name = "JOHN STOP SCREAMING.mid"

	#1 gets the vertex data
	#2 gets the vertex and edge data
	#3 gets vertex, edge and face data.
	#Anything else returns an empty array
	data = get_data(3, name)

	#This is the name of the mesh that will be instantiated when you press "Run Script" in Blender
	mesh = bpy.data.meshes.new(name="New Test Mesh " + str(test_id))
	mesh.from_pydata(data[0], data[1], data[2])
	# useful for development when the mesh may be invalid or has faulty geometry
	# mesh.validate(verbose=True)
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
		text="Soundspire " + str(test_id),
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