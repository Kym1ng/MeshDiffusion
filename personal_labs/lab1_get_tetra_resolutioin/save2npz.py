import numpy as np
def read_tet_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # First line contains the counts
    header = lines[0].strip().split()
    num_vertices = int(header[1])
    num_tetrahedra = int(header[2])

    # Read vertices
    vertices = []
    for i in range(1, num_vertices + 1):
        parts = lines[i].strip().split()
        vertices.append([float(x) for x in parts])

    # Read tetrahedra
    tetrahedra = []
    for i in range(num_vertices + 1, num_vertices + 1 + num_tetrahedra):
        parts = lines[i].strip().split()
        tetrahedra.append([int(x) for x in parts])

    return np.array(vertices), np.array(tetrahedra)

def save_to_npz(vertices, tetrahedra, output_file_path):
    np.savez(output_file_path, vertices=vertices, tetrahedra=tetrahedra)

# Example usage
tet_file_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.tet'
output_file_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.npz'

vertices, tetrahedra = read_tet_file(tet_file_path)
save_to_npz(vertices, tetrahedra, output_file_path)
print(f"Read {len(vertices)} vertices and {len(tetrahedra)} tetrahedra")
print(f"Saved .npz file to {output_file_path}")
