import bpy
from VisIt.lib import global_consts

class CameraLibrary(bpy.types.Panel):
    bl_label = "Camera Library"
    bl_idname = "VIS_IT_PT_camera_library"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE
    bl_parent_id = global_consts.MAIN_PANEL_ID

    def draw(self, context):
        layout = self.layout

        layout.label(text="This is the camera library")