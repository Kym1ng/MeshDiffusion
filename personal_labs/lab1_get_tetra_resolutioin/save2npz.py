import numpy as np

def read_tet_file(tet_file_path):
    """
    Read a .tet file and extract vertices and tetrahedra information.
    
    Args:
    - tet_file_path (str): Path to the .tet file.
    
    Returns:
    - vertices (np.ndarray): Array of vertices.
    - tetrahedra (np.ndarray): Array of tetrahedra.
    """
    vertices = []
    tetrahedra = []

    with open(tet_file_path, 'r') as file:
        lines = file.readlines()
        vertex_section = False
        tetrahedron_section = False

        for line in lines:
            if line.startswith("Vertices"):
                vertex_section = True
                continue
            elif line.startswith("Tetrahedra"):
                vertex_section = False
                tetrahedron_section = True
                continue

            if vertex_section:
                parts = line.strip().split()
                if len(parts) == 3:
                    vertices.append([float(parts[0]), float(parts[1]), float(parts[2])])
            elif tetrahedron_section:
                parts = line.strip().split()
                if len(parts) == 4:
                    tetrahedra.append([int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])])

    return np.array(vertices), np.array(tetrahedra)

def save_to_npz(vertices, tetrahedra, output_file_path):
    """
    Save vertices and tetrahedra information to a .npz file.
    
    Args:
    - vertices (np.ndarray): Array of vertices.
    - tetrahedra (np.ndarray): Array of tetrahedra.
    - output_file_path (str): Path to the output .npz file.
    """
    np.savez(output_file_path, vertices=vertices, tetrahedra=tetrahedra)

# Example usage
tet_file_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.tet'
output_file_path = '/Users/minggh/Documents/USC_ADS/lab_Doc_Shi/code/shapeDiffusion/MeshDiffusion/personal_labs/lab1_get_tetra_resolutioin/left_hippocampus_mesh.npz'

vertices, tetrahedra = read_tet_file(tet_file_path)
save_to_npz(vertices, tetrahedra, output_file_path)

print(f"Saved .npz file to {output_file_path}")
