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
from VisIt.lib.collection_props import InitialisedScenesItem

_types = {
    "string": bpy.props.StringProperty,
    "int": bpy.props.IntProperty,
    "bool": bpy.props.BoolProperty,
    "collection": bpy.props.CollectionProperty
}

_prop_names = {}

def _create_prop(blender_ID, prop_name, prop_type, **kwargs):
    """Create and register a custom prop on a Blender ID data type"""

    if prop_type not in _types:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return
    
    if blender_ID in _prop_names and prop_name in _prop_names[blender_ID]:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return
    
    if blender_ID not in _prop_names:
        _prop_names[blender_ID] = []

    _prop_names[blender_ID].append(prop_name)

    setattr(
        blender_ID,
        prop_name,
        _types[prop_type](**kwargs)
    )

def _remove_prop(blender_ID, prop_name):
    """Delete and unregister a custom prop"""

    if blender_ID not in _prop_names or prop_name not in _prop_names[blender_ID]:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return

    _prop_names[blender_ID].remove(prop_name)

    delattr(blender_ID, prop_name)

def _remove_all_props():
    """Delete and unregister all custom props"""

    for blender_ID in _prop_names:
        for prop_name in _prop_names[blender_ID]:
            delattr(blender_ID, prop_name)
    
    _prop_names.clear()

def add_custom_props():
    """Create all the required custom props"""

    _create_prop(
        bpy.types.WindowManager,
        "initialised_scenes",
        "collection",
        type=InitialisedScenesItem,
        name="Initialised scenes",
        description="A collection of all the initialised scenes in the file",
    )
    _create_prop(
        bpy.types.WindowManager,
        "scene_selection_index",
        "int",
        name="Scene selection index",
        description="Store the index of the selected scene in the UI list",
        min=0,
        step=1,
    )
    _create_prop(
        bpy.types.Scene,
        "initialised",
        "bool",
        name="Initialised",
        description="Define whether the scene is a VisIt initialised scene or not",
        default=False
    )
    _create_prop(
        bpy.types.Scene,
        "render_scene",
        "bool",
        name="Render scene",
        description="Toggle scene in renders",
        default=True
    )
    _create_prop(
        bpy.types.Scene,
        "scene_prefix",
        "string",
        name="Scene prefix",
        description="Define a prefix to be added to the name of each scene",
        default="sc"
    )
    _create_prop(
        bpy.types.Scene,
        "scene_padding",
        "int",
        name="Scene name padding",
        description="Define length of the numerical suffix of the scene name",
        min=1,
        max=10,
        step=1,
        default=1
    )
    _create_prop(
        bpy.types.Scene,
        "shot_prefix",
        "string",
        name="Shot prefix",
        description="Define a prefix to be added to the name of each shot",
        default="sh"
    )
    _create_prop(
        bpy.types.Scene,
        "shot_padding",
        "int",
        name="Shot name padding",
        description="Define length of the numerical suffix of the shot name",
        min=1,
        max=10,
        step=1,
        default=1
    )
    _create_prop(
        bpy.types.Scene,
        "render_dir",
        "string",
        name="Render directory",
        description="Choose a render directory for your shots",
        subtype='DIR_PATH',
    )
    _create_prop(
        bpy.types.Scene,
        "frame_padding",
        "int",
        name="Frame padding",
        description="Define length of frame number part of the render filename",
        min=1,
        max=10,
        step=1,
        default=1
    )
    _create_prop(
        bpy.types.Scene,
        "camera_selection_index",
        "int",
        name="Camera index",
        description="Store the index of the selected camera in the UI list",
        min=0,
        step=1
    )
    _create_prop(
        bpy.types.Camera,
        "render_camera",
        "bool",
        name="Render camera",
        description="Toggle camera in renders",
        default=True
    )

def delete_custom_props():
    """Delete all the existing custom props"""

    _remove_all_props()