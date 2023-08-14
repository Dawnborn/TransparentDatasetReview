import bpy

n_kp = 8
for obj in  bpy.data.collections['Chemical'].objects:
    bpy.data.collections['Chemical'].objects.unlink(obj)

for obj in  bpy.data.collections['Household'].objects:
    bpy.data.collections['Household'].objects.unlink(obj)

for obj in bpy.data.objects:
    print(obj)
    object_name = obj.name
    if not "_kp" in object_name:
        if object_name in bpy.data.collections:
            object_collection = bpy.data.collections[object_name]
        else:
            object_collection = bpy.data.collections.new(object_name)
        parent_collection = bpy.data.objects[object_name].users_collection[0]
        
        if object_name != parent_collection.name:
            parent_collection.children.link(object_collection)
        if object.name not in object_collection.objects:
            object_collection.objects.link(object)
    
    obj_loc = bpy.data.objects[object_name].location
    obj_dim = bpy.data.objects[object_name].dimension
    x, y, zmin, zmax = obj_loc.x, obj_loc.y, obj_loc.z - obj_dim.z / 2, obj_loc.z + obj_dim.z / 2
    for i in range(n_kp):
        z = zmin + (zmax - zmin) / (n_kp - 1) * i
        kp_name = f"{object_name}_kp{i}"
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.001, enter_editmode=False,  align='WORLD', location=(x, y, z), scale=(1, 1, 1))
        bpy.data.objects['Sphere'].name = kp_name
        object_collection.objects.link(bpy.data.objects[kp_name])
        bpy.data.scenes['Scene'].collection.objects.unlink(bpy.data.objects[kp_name])
        bpy.data.objects[kp_name].location = (x, y, z)
    break