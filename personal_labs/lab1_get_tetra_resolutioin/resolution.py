import numpy as np
import torch

import torch
print(torch.__version__)


# Load the tetrahedral mesh
# find the size of the bounding box
# calculate the resolution of the mesh object = size / spacing

# Load the tetrahedral mesh
tet_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.npz'
tet = np.load(tet_path)
print(tet['vertices'])

# Find the size of the bounding box
vertices = torch.tensor(tet['vertices'])

