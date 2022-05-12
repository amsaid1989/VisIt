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

class InitialiseProjectOperator(bpy.types.Operator):
    bl_idname = "vis_it.initialise_project"
    bl_label = "Initialise Project"
    bl_description = "Initialises the Blender file as a VisIt project"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        area = context.area

        return area.type == 'VIEW_3D'

    def _purge_blend_file_data(self, context):
        for sc in bpy.data.scenes:
            if sc != context.scene:
                bpy.data.scenes.remove(sc)
        for col in bpy.data.collections:
            bpy.data.collections.remove(col)
        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj)
        for cam in bpy.data.cameras:
            bpy.data.cameras.remove(cam)
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh)
        for world in bpy.data.worlds:
            bpy.data.worlds.remove(world)
        for mat in bpy.data.materials:
            bpy.data.materials.remove(mat)
        for light in bpy.data.lights:
            bpy.data.lights.remove(light)

    def execute(self, context):
        self._purge_blend_file_data(context)

        scene = context.scene
        wm = context.window_manager
        
        scene.initialised = True
        item = wm.initialised_scenes.add()
        item.scene_name = scene.name

        return {'FINISHED'}