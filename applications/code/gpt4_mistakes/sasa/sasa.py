import numpy as np
import sys
import os

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")

def compute_sasa_mdtraj(pdb_file):
    import mdtraj as md
    pdb = md.load(pdb_file)
    
    sasa = md.shrake_rupley(pdb,mode='residue')
    return sasa

my_sasa = compute_sasa_mdtraj(pdb_file)
nlcc_sasa = protein_surface_area(pdb_file)

#print("My result:", my_sasa)
#print("nlcc result", nlcc_sasa)

result = True if np.abs( my_sasa.mean() - nlcc_sasa.mean() )<0.1 else False
