import bpy
from VisIt.lib import global_consts

class ProjectSettings(bpy.types.Panel):
    bl_label = "Project Settings"
    bl_idname = "VIS_IT_PT_project_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE
    bl_parent_id = global_consts.MAIN_PANEL_ID

    @staticmethod
    def _draw_framerate_label(render):
        selected_item_label = bpy.types.RENDER_MT_framerate_presets.bl_label

        if render.fps_base == 1.0:
            fps_rate = round(render.fps)
        else:
            fps_rate = round(render.fps / render.fps_base, 2)
        
        custom_framerate = (fps_rate not in {23.98, 24, 25, 29.97, 30, 50, 59.94, 60, 120, 240})

        if custom_framerate:
            display_label = f"Custom ({fps_rate} fps)"
            show_framerate = True
        else:
            display_label = f"{fps_rate} fps"
            show_framerate = (selected_item_label == "Custom")
        
        return display_label, show_framerate

    @staticmethod
    def draw_framerate_settings(layout, render):
        args = render.fps, render.fps_base

        label, show_framerate = ProjectSettings._draw_framerate_label(render)

        layout.menu("RENDER_MT_framerate_presets", text=label)

        if show_framerate:
            layout.prop(render, "fps")
            layout.prop(render, "fps_base", text="Base")

    def draw(self, context):
        scene = context.scene

        layout = self.layout

        row = layout.row()
        row.operator("vis_it.initialise_project")

        box = layout.box()
        box.label(text="Scene settings", icon='SCENE_DATA')
        box.prop(scene, "scene_prefix")
        box.prop(scene, "scene_padding")

        box = layout.box()
        box.label(text="Shot settings", icon='OUTLINER_OB_CAMERA')
        box.prop(scene, "shot_prefix")
        box.prop(scene, "shot_padding")

        box = layout.box()
        box.label(text="Render settings", icon='OUTPUT')
        box.prop(scene.render, "resolution_x")
        box.prop(scene.render, "resolution_y")
        box.prop(scene.render, "resolution_percentage")
        self.draw_framerate_settings(box, scene.render)
        box.prop(scene, "render_dir")
        box.prop(scene, "frame_padding")
        box.prop(scene.render.image_settings, "file_format")
        box.prop(scene.render.image_settings, "color_mode")
        box.prop(scene.render.image_settings, "color_depth")