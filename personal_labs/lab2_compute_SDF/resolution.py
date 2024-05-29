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

# Find the size of the bounding box
vertices = torch.tensor(tet['vertices'])
min_coords, _ = torch.min(vertices, dim=0)
max_coords, _ = torch.max(vertices, dim=0)
size = max_coords - min_coords
print('The size of the bounding box is: ', size)

# import numpy as np
# import os
# import torch

# import torch
# print(torch.__version__)


# # Load the tetrahedral mesh
# # find the size of the bounding box
# # calculate the resolution of the mesh object = size / spacing

# # Load the tetrahedral mesh
# tet_path = '/scratch/faculty/shi/spectrum/Student_2024/haoming/MeshDiffusion/ShapeDiffusion/tetGrid_npz_data'

# count = 0
# total_files = 0
# for obj, date, files in os.walk(tet_path):
#     for file in files:
#         if file.endswith(".npz"):
#             total_files += 1

# sizes = []
# for obj, date, files in os.walk(tet_path):
#         for file in files:
#             if file.endswith(".npz"):
#                 tet_file_path = os.path.join(obj, file)
#                 # print(tet_file_path)
#                 tet = np.load(tet_file_path)
#                 # # Find the size of the bounding box
#                 vertices = torch.tensor(tet['vertices'])
#                 min_coords, _ = torch.min(vertices, dim=0)
#                 max_coords, _ = torch.max(vertices, dim=0)
#                 size = max_coords - min_coords
#                 sizes.append(size)
#                 print(f'conveted {count} / {total_files}')
#                 count += 1


# # Find the largest size
# largest_size = max(sizes, key=lambda s: s.prod().item())
# print('The largest size of the bounding box is:', largest_size)

# spacing = 0.5
# resolution = largest_size / spacing
# print('The resolution of the mesh object is:', resolution)


# The largest size of the bounding box is: tensor([28.3548, 31.8948, 43.1179], dtype=torch.float64)
# The resolution of the mesh object is: tensor([56.7096, 63.7896, 86.2358], dtype=torch.float64)
