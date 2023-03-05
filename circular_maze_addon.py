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
    
    # Select the first face
    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()
    bm.faces[0].select_set(True)
    
    mat = bpy.data.materials.new(name="Material")
    mat.diffuse_color = (0, 0, 1, 1) # Blue color
    obj.data.materials.append(mat)
    
    # Assign the new material to the selected face(s)
    bpy.ops.object.material_slot_assign()
    
    # Show the updates in the viewport
    bmesh.update_edit_mesh(bpy.context.object.data)
    
    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')
    

CreateCylinder(6)