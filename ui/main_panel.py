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

class MainPanel(bpy.types.Panel):
    bl_label = global_consts.PACKAGE
    bl_idname = global_consts.MAIN_PANEL_ID
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = global_consts.PACKAGE

    initial_draw = True

    @staticmethod
    def load_initialised_scenes(context):
        wm = context.window_manager

        for scene in context.blend_data.scenes:
            if scene.initialised:
                item = wm.initialised_scenes.add()
                item.scene_name = scene.name
        
        MainPanel.initial_draw = False

    def draw(self, context):
        if MainPanel.initial_draw:
            MainPanel.load_initialised_scenes(context)