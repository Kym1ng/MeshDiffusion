import meshio
import numpy as np

def calculate_bcc_grid_resolution(mesh):
    # Calculate the bounding box size
    bounding_box = mesh.bounds
    size = np.abs(bounding_box[1] - bounding_box[0])
    # Calculate the resolution = size / spacing
    resolution = size / mesh.spacing
    print('The resolution of the mesh object is: ', resolution)
    
    
# Load the tetrahedral mesh
# whats the error here?
filepath = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.tet'
# filepath = 'MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.tet'
mesh = meshio.read(filepath)