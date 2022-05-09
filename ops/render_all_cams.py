import os
import bpy
from VisIt.lib import render_utils

class RenderAllCamsOperator(bpy.types.Operator):
    bl_idname = "vis_it.render_all_cams"
    bl_label = "Render all cams"
    bl_description = "Render all cameras in a scene as separate shots"
    bl_options = {'REGISTER', 'BLOCKING'}

    frame_padding: bpy.props.IntProperty(
        name="Frame padding",
        default=1,
        min=1,
        step=1,
    )

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        wm = context.window_manager
        scene = context.scene
        previz_render_path = scene.render_dir
        scene_render_path = scene.render.filepath

        if len(previz_render_path.strip()) == 0:
            self.report({'ERROR'}, "Please choose a render directory")
            return {'CANCELLED'}

        cams = render_utils.get_scene_cameras(scene)
        override = {}

        for cam in cams:
            scene.camera = cam
            filename = f"{cam.name}_{'#' * self.frame_padding}"
            scene.render.filepath = os.path.join(previz_render_path, scene.name, cam.name, filename)

            bpy.ops.render.view_show('INVOKE_DEFAULT')
            bpy.ops.render.render(animation=True)
            bpy.ops.render.view_cancel('INVOKE_DEFAULT')
        
        scene.render.filepath = scene_render_path

        return {'FINISHED'}