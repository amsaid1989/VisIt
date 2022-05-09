import bpy

_types = {
    "string": bpy.props.StringProperty,
    "int": bpy.props.IntProperty
}

_prop_names = []
_prop_values = {}

def _create_prop(prop_name, prop_type, **kwargs):
    """Create and register a custom prop on all relevant Blender data types"""

    if prop_type not in _types:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return
    
    if prop_name in _prop_names:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return
    
    def on_wm_prop_update(self, context):
        sync_all_scenes_with_win_manager(context)
    
    def on_scene_prop_update(self, context):
        sync_win_manager_with_scene(context)

    _prop_names.append(prop_name)

    if "update" in kwargs:
        kwargs.pop("update")
    
    scene_prop = setattr(
        bpy.types.Scene,
        prop_name,
        _types[prop_type](**kwargs, update=on_scene_prop_update)
    )
    wm_prop = setattr(
        bpy.types.WindowManager,
        prop_name,
        _types[prop_type](**kwargs, update=on_wm_prop_update)
    )

    _prop_values[prop_name] = {
        "scene": scene_prop,
        "wm": wm_prop
    }

def _remove_prop(prop_name):
    """Delete and unregister a custom prop"""

    if prop_name not in _prop_names:
        """
        TODO (Abdelrahman): Raise an appropriate exception here
        """
        return

    _prop_names.remove(prop_name)
    _prop_values.pop(prop_name)

    delattr(bpy.types.Scene, prop_name)
    delattr(bpy.types.WindowManager, prop_name)

def _remove_all_props():
    """Delete and unregister all custom props"""

    for prop_name in _prop_names:
        delattr(bpy.types.Scene, prop_name)
        delattr(bpy.types.WindowManager, prop_name)
    
    _prop_names.clear()
    _prop_values.clear()

def sync_all_scenes_with_win_manager(context):
    """
    Make sure all scenes have the same values for the custom props
    by getting the value of each prop from the window manager
    """

    for scene in bpy.data.scenes:
        for prop_name in _prop_names:
            scene_value = getattr(scene, prop_name)
            wm_value = getattr(context.window_manager, prop_name)

            if scene_value != wm_value:
                setattr(scene, prop_name, wm_value)

def sync_win_manager_with_scene(context):
    """
    Update all custom props' values in the window manager using
    the values of the current scene
    """

    for prop_name in _prop_names:
        scene_value = getattr(context.scene, prop_name)
        wm_value = getattr(context.window_manager, prop_name)

        if wm_value != scene_value:
            setattr(context.window_manager, prop_name, scene_value)

def add_custom_props():
    """Create all the required custom props"""

    _create_prop(
        "scene_prefix",
        "string",
        name="Scene prefix",
        description="Define a prefix to be added to the name of each scene",
        default="sc"
    )
    _create_prop(
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
        "shot_prefix",
        "string",
        name="Shot prefix",
        description="Define a prefix to be added to the name of each shot",
        default="sh"
    )
    _create_prop(
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
        "render_dir",
        "string",
        name="Render directory",
        description="Choose a render directory for your shots",
        subtype='DIR_PATH',
    )
    _create_prop(
        "frame_padding",
        "int",
        name="Frame padding",
        description="Define length of frame number part of the render filename",
        min=1,
        max=10,
        step=1,
        default=1
    )

def delete_custom_props():
    """Delete all the existing custom props"""

    _remove_all_props()