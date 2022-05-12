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

bl_info = {
    "name": "VisIt",
    "author": "Abdelrahman Said",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "",
    "description": "Example Add-on",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "3D View",
}

import os
import bpy
from VisIt.preferences import VisItPreferences
from VisIt import lib
from VisIt.lib import custom_props_utils
from VisIt import ops
from VisIt import ui

classes = [
    VisItPreferences,
    *lib.classes,
    *ops.classes,
    *ui.classes
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    custom_props_utils.add_custom_props()
    bpy.types.Scene.render_progress = bpy.props.FloatProperty(name="progress", subtype='PERCENTAGE', min=0, max=100)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    custom_props_utils.delete_custom_props()
    del bpy.types.Scene.render_progress

def main():
    try:
        register()
    except:
        unregister()
        register()