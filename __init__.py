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
from VizIt.ops.render_all_cams import  RenderAllCamsOperator
from VizIt.ui.test_panel import TestPanel

classes = [
    VizItPreferences,
    RenderAllCamsOperator,
    TestPanel
]

def add_custom_props():
    bpy.types.WindowManager.render_dir = bpy.props.StringProperty(
        name="Render directory",
        description="Choose a render directory for your shots",
        subtype='DIR_PATH',
    )

    bpy.types.WindowManager.frame_padding = bpy.props.IntProperty(
        name="Frame padding",
        description="Define length of frame number part of the render filename",
        min=1,
        max=10,
        step=1,
        default=1
    )

def remove_custom_props():
    del bpy.types.WindowManager.render_dir
    del bpy.types.WindowManager.frame_padding

def register():
    add_custom_props()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    remove_custom_props()

    for cls in classes:
        bpy.utils.unregister_class(cls)

def main():
    try:
        register()
    except:
        unregister()
        register()