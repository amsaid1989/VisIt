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