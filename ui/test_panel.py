import bpy
from VizIt.lib import global_consts

class TestPanel(bpy.types.Panel):
    bl_label = "Test panel"
    bl_idname = "VIEW_3D_PT_test_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VizIt'

    def draw(self, context):
        layout = self.layout

        wm = context.window_manager
        
        row = layout.row()
        row.prop(wm, "render_dir")

        row = layout.row()
        row.prop(wm, "frame_padding")
        
        row = layout.row()
        render_op = row.operator(operator="render.render_all_cams", icon='RENDER_ANIMATION')
        render_op.frame_padding = wm.frame_padding