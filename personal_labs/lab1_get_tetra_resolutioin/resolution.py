import numpy as np
import torch

tet_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.npz'
tet = np.load(tet_path)
vertices = torch.tensor(tet['vertices'])
vertices_unique = vertices[:].unique()
dx = vertices_unique[1] - vertices_unique[0]

vertices_discretized = (torch.round(
    (vertices - vertices.min()) / dx)
).long()
        
data_all = np.load(FLAGS.sample_path)
print('shape of generated data', data_all.shape)
