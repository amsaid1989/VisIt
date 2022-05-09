import bpy
from VisIt.lib import global_consts

class MainPanel(bpy.types.Panel):
    bl_label = global_consts.PACKAGE
    bl_idname = global_consts.MAIN_PANEL_ID
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE

    def draw(self, context):
        pass