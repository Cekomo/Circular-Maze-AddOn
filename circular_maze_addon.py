import bpy
import bmesh

def CreateCylinder(r):
    n_verts = r * 15 # vertices should be propotional to the radius
    if (n_verts < 30): 
        n_verts = 30
    # Create a new cylinder mesh
    bpy.ops.mesh.primitive_cylinder_add(radius = (r + 0.5), depth = 0.2, vertices = n_verts)
    obj = bpy.context.object # Get a reference to the cylinder object    
    obj.location = (0, 0, 0) # Move the cylinder to a new location

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')

    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    for f in bm.faces:
        if f.normal.z > 0.9:  # adjust threshold as needed
            f.select = True
            break
        
    bmesh.update_edit_mesh(me)
    
    # Exit edit mode
    # bpy.ops.object.mode_set(mode='OBJECT')
    

CreateCylinder(6)