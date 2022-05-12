# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

import os
import time
import bpy
from bpy.app.handlers import persistent
from VisIt.lib import render_utils

@persistent
def post_handler(frame):
    context = bpy.context

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

    def __init__(self):
        self.timer = None

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def invoke(self, context, event):
        wm = context.window_manager
        self.timer = wm.event_timer_add(1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            bpy.app.handlers.render_post.append(post_handler)

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

                # bpy.ops.render.view_show('INVOKE_DEFAULT')
                bpy.ops.render.render(animation=True)
                # bpy.ops.render.view_cancel('INVOKE_DEFAULT')
            
            scene.render.filepath = scene_render_path
            bpy.app.handlers.render_post.remove(post_handler)

            return {'FINISHED'}
        
        return {'PASS_THROUGH'}
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self.timer)