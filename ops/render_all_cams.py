import os
import bpy
from VizIt.lib import render_utils

class RenderAllCamsOperator(bpy.types.Operator):
    bl_idname = "render.render_all_cams"
    bl_label = "Render all cams"
    bl_description = "Render all cameras in a scene as separate shots"
    bl_options = {'REGISTER', 'BLOCKING'}

    frame_padding: bpy.props.IntProperty(
        name="Frame padding",
        default=1,
        min=1,
        step=1,
    )

    def execute(self, context):
        wm = context.window_manager
        previz_render_path = wm.render_dir

        if len(previz_render_path.strip()) == 0:
            self.report({'ERROR'}, "Please choose a render directory")
            return {'CANCELLED'}

        scene = context.scene
        scene_render_path = scene.render.filepath
        cams = render_utils.get_scene_cameras(scene)

        for cam in cams:
            scene.camera = cam
            filename = f"{cam.name}_{'#' * self.frame_padding}"
            scene.render.filepath = os.path.join(previz_render_path, scene.name, cam.name, filename)

            bpy.ops.render.render(animation=True)
        
        scene.render.filepath = scene_render_path

        return {'FINISHED'}