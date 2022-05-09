import bpy
from VisIt.lib import global_consts

class SceneManager(bpy.types.Panel):
    bl_label = "Scene Manager"
    bl_idname = "VIS_IT_PT_scene_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE
    bl_parent_id = global_consts.MAIN_PANEL_ID

    def draw(self, context):
        layout = self.layout

        layout.label(text="This is the scene manager")