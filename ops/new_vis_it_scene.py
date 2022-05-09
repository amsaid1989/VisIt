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