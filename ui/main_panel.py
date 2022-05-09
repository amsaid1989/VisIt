import bpy
from VisIt.lib import global_consts

class MainPanel(bpy.types.Panel):
    bl_label = global_consts.PACKAGE
    bl_idname = global_consts.MAIN_PANEL_ID
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE

    initial_draw = True

    @staticmethod
    def load_initialised_scenes(context):
        wm = context.window_manager

        for scene in context.blend_data.scenes:
            if scene.initialised:
                item = wm.initialised_scenes.add()
                item.scene_name = scene.name
        
        MainPanel.initial_draw = False

    def draw(self, context):
        if MainPanel.initial_draw:
            MainPanel.load_initialised_scenes(context)