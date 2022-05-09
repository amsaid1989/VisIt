import bpy

class InitialiseProjectOperator(bpy.types.operator):
    bl_idname = "vis_it.initialise_project"
    bl_label = "Initialise Project"
    bl_description = "Initialises the Blender file as a VisIt project"
    bl_options = {'REGISTER'}

    index = 0

    @classmethod
    def poll(cls, context):
        area = context.area

        return area.type == 'VIEW_3D'

    def execute(self, context):
        pass