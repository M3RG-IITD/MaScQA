import numpy as np
from Bio.PDB import PDBParser

def pairwise_dist(pdb_file):
    """
    This function loads a pdb
    Selects only the alpha carbons
    Calculates the number of unique alpha carbon pairs
    Returns the distances between each alpha carbon pair
    """
    # Load the pdb file
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb_file)

    # Select only the alpha carbons
    alpha_carbons = [atom for atom in structure.get_atoms() if atom.get_name() == 'CA']

    # Calculate the number of unique alpha carbon pairs
    num_pairs = len(alpha_carbons) * (len(alpha_carbons) - 1) // 2

    # Calculate the distances between each alpha carbon pair
    distances = np.zeros((num_pairs,))
    for i in range(len(alpha_carbons)):
        for j in range(i+1, len(alpha_carbons)):
            distances[i * len(alpha_carbons) + j - ((i+1)*(i+2))//2] = alpha_carbons[i] - alpha_carbons[j]

    return distances