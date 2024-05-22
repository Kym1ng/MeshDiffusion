# This folder is to check the resolution of the mesh object.
# We have already have the mesh.obj in the folder.
# We will check the resolution of the mesh object by finding the size of boundry box of the mesh object.

# first we will import the necessary libraries
import numpy as np
import trimesh

# Load the mesh object
mesh1 = trimesh.load_mesh('/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/left_hippocampus_mesh.obj')
mesh2 = trimesh.load_mesh('/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/left_hippocampus_mesh1.obj')

# # Find the boundry box of the mesh object
# boundry_box1 = mesh1.bounding_box.bounds
# boundry_box2 = mesh2.bounding_box.bounds

# # Find the size of the boundry box
# size1 = np.abs(boundry_box1[0] - boundry_box1[1])
# size2 = np.abs(boundry_box2[0] - boundry_box2[1])

# Create mesh representations of the bounding boxes
# bbox1_mesh = trimesh.creation.box(extents=size1, transform=trimesh.transformations.translation_matrix((boundry_box1[1] + boundry_box1[0]) / 2))
# # Save the bounding box meshes as .obj files
# bbox1_mesh.export('bounding_box1.obj')

import meshio

def calculate_bcc_grid_resolution(mesh):
    # Calculate the bounding box size
    bounding_box = mesh.bounds
    size = np.abs(bounding_box[1] - bounding_box[0])
    
    # Number of tetrahedra
    num_tetrahedra = len(mesh.cells_dict['tetra'])
    
    # Assuming the mesh is a BCC grid
    # The number of grid points in a BCC lattice can be estimated from the number of tetrahedra
    # Each tetrahedron in a BCC lattice typically corresponds to one cell
    # The number of grid points is roughly proportional to the cube root of the number of cells
    num_points_x = int(np.round(num_tetrahedra ** (1/3)))
    num_points_y = int(np.round(num_tetrahedra ** (1/3)))
    num_points_z = int(np.round(num_tetrahedra ** (1/3)))
    
    # Calculate the resolution
    resolution_x = size[0] / (num_points_x - 1)
    resolution_y = size[1] / (num_points_y - 1)
    resolution_z = size[2] / (num_points_z - 1)
    
    return num_points_x, num_points_y, num_points_z, resolution_x, resolution_y, resolution_z

# Load the tetrahedral mesh
mesh = meshio.read('/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/left_hippocampus_mesh.tet')

# Calculate the grid resolution
num_points_x, num_points_y, num_points_z, resolution_x, resolution_y, resolution_z = calculate_bcc_grid_resolution(mesh)

print(f"Grid resolution along x-axis: {num_points_x} points with spacing {resolution_x}")
print(f"Grid resolution along y-axis: {num_points_y} points with spacing {resolution_y}")
print(f"Grid resolution along z-axis: {num_points_z} points with spacing {resolution_z}")
