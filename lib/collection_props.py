import bpy

class InitialisedScenesItem(bpy.types.PropertyGroup):
    scene_name: bpy.props.StringProperty(name="Scene")