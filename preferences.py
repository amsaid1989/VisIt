import os
import bpy
from VisIt.lib import global_consts

class VisItPreferences(bpy.types.AddonPreferences):
    bl_idname = global_consts.PACKAGE

    filepath = os.path.dirname(os.path.abspath(__file__))