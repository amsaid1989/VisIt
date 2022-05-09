import bpy
from VisIt.lib import global_consts

class SCENE_MANAGER_UL_vis_it_scenes(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        scene = bpy.data.scenes[item.scene_name]

        if scene.initialised:
            if scene.render_scene:
                icon = 'RESTRICT_RENDER_OFF'
            else:
                icon = 'RESTRICT_RENDER_ON'

            if self.layout_type in {'DEFAULT', 'COMPACT'}:
                row = layout.row()
                row.label(text=scene.name, icon='SCENE_DATA')

                row.prop(scene, "render_scene", text="", icon=icon, emboss=False)
            elif self.layout_type in {'GRID'}:
                layout.prop(scene, "render_scene", text="", icon=icon, emboss=False)

class SceneManager(bpy.types.Panel):
    bl_label = "Scene Manager"
    bl_idname = "VIS_IT_PT_scene_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE
    bl_parent_id = global_consts.MAIN_PANEL_ID

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("vis_it.new_scene")

        wm = context.window_manager

        row = layout.row()
        row.template_list("SCENE_MANAGER_UL_vis_it_scenes", "", wm, "initialised_scenes", wm, "scene_selection_index")