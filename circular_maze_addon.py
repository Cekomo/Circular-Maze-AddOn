import bpy

def CreateCylinder(r):
    n_verts = r * 15 # vertices should be propotional to the radius
    # Create a new cylinder mesh
    bpy.ops.mesh.primitive_cylinder_add(radius = (r + 0.5), depth = 0.2, vertices = n_verts)
    obj = bpy.context.object # Get a reference to the cylinder object    
    obj.location = (0, 0, 0) # Move the cylinder to a new location

CreateCylinder(6)