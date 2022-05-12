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

import bpy
from VisIt.lib.scene_index import SceneIndex

class NewVisItSceneOperator(bpy.types.Operator):
    bl_idname = "vis_it.new_scene"
    bl_label = "Add scene"
    bl_description = "Create a new VisIt scene"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        area = context.area

        return area.type == 'VIEW_3D'
    
    def execute(self, context):
        bpy.ops.scene.new(type='EMPTY')

        scene = context.scene
        wm = context.window_manager

        scene.initialised = True
        item = wm.initialised_scenes.add()
        item.scene_name = scene.name

        return {'FINISHED'}