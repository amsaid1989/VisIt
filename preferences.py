import os
import bpy
from VizIt.lib import global_consts

class VizItPreferences(bpy.types.AddonPreferences):
    bl_idname = global_consts.PACKAGE

    filepath = os.path.dirname(os.path.abspath(__file__))
    # frame_padding: bpy.props.IntProperty(
    #     name="Frame padding",
    #     description="Define length of frame number part of the render filename",
    #     min=1,
    #     step=1,
    #     default=1
    # )