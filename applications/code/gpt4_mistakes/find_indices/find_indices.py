import os
import numpy as np

pdb_file = os.path.join(_FILE_DIR_,"1l2y.pdb")

def get_pair_indices(pdb_file):
    import mdtraj as md
    pdb = md.load(pdb_file)
    top = pdb.topology
    CAs = [atom.index for atom in top.atoms if atom.name == 'CA']
    indices_pair = np.array([CAs[0], CAs[1]])
    return indices_pair

my_indices_pair = get_pair_indices(pdb_file)
prompt_indices_pair = get_ca_indices(pdb_file)

result = True if np.all(my_indices_pair == prompt_indices_pair) else False


