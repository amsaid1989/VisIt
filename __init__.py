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
from VisIt.lib import custom_props_utils
from VisIt import ops
from VisIt import ui

classes = [
    VisItPreferences,
    *ops.classes,
    *ui.classes
]

def register():
    custom_props_utils.add_custom_props()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    custom_props_utils.delete_custom_props()

    for cls in classes:
        bpy.utils.unregister_class(cls)

def main():
    try:
        register()
    except:
        unregister()
        register()