import bpy
from VisIt.lib import global_consts

class RenderManager(bpy.types.Panel):
    bl_label = "Render Manager"
    bl_idname = "VIS_IT_PT_render_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE
    bl_parent_id = global_consts.MAIN_PANEL_ID

    def draw(self, context):
        layout = self.layout

        render = layout.operator("vis_it.render_all_cams")
        render.frame_padding = context.scene.frame_padding