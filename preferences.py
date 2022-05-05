import os
import bpy

class VizItPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    filepath = os.path.dirname(os.path.abspath(__file__))