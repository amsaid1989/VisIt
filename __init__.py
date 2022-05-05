bl_info = {
    "name": "VizIt",
    "author": "Abdelrahman Said",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "",
    "description": "Example Add-on",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object",
}

import os
import bpy
from VizIt.preferences import VizItPreferences

classes = [
    VizItPreferences,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

def main():
    try:
        register()
    except:
        unregister()
        register()