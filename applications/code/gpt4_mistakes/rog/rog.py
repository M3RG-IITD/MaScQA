import numpy as np
import sys
import os

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")

def compute_rg_mdtraj(pdb_file):
    import mdtraj as md
    pdb = md.load(pdb_file)
    rg = md.compute_rg(pdb)
    return rg

my_rg = compute_rg_mdtraj(pdb_file)
nlcc_rg = protein_radius_of_gyration(pdb_file)

#print("My result:", my_rg)
#print("nlcc result", nlcc_rg)

result = True if np.abs( my_rg - nlcc_rg )<0.1 else False

