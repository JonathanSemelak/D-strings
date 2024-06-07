import numpy as np

def calculate_dihedral(trajectory, i, j, k, l):
    dihedrals = []
    for step in trajectory:
        A = step[i]
        B = step[j]
        C = step[k]
        D = step[l]

        v1 = B - A
        v2 = C - B
        v3 = D - C

        n1 = np.cross(v1, v2)
        n2 = np.cross(v2, v3)

        n1_mag = np.linalg.norm(n1)
        n2_mag = np.linalg.norm(n2)

        cos_phi = np.dot(n1, n2) / (n1_mag * n2_mag)
        phi = np.arccos(np.clip(cos_phi, -1.0, 1.0)) # Clip for numerical stability

        phi_deg = np.degrees(phi)
        dihedrals.append(phi_deg+180.0)

    return np.array(dihedrals)

