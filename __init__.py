bl_info = {
    "name": "VisIt",
    "author": "Abdelrahman Said",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "",
    "description": "Example Add-on",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "3D View",
}

import os
import bpy
from VisIt.preferences import VisItPreferences
from VisIt import lib
from VisIt.lib import custom_props_utils
from VisIt import ops
from VisIt import ui

classes = [
    VisItPreferences,
    *lib.classes,
    *ops.classes,
    *ui.classes
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    custom_props_utils.add_custom_props()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    custom_props_utils.delete_custom_props()

def main():
    try:
        register()
    except:
        unregister()
        register()