import bpy

def get_scene_cameras(scene: bpy.types.Scene):
    cams = []

    for obj in scene.collection.all_objects:
        if obj.type == 'CAMERA':
            cams.append(obj)
    
    return cams