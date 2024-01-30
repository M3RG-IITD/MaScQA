def protein_radius_of_gyration(pdb_file):
   """
   1. This function loads a pdb
   2. Calculates the radius of gyration
   3. Returns it
   """
   from Bio.PDB import PDBParser
   from Bio.PDB.Polypeptide import is_aa
   import numpy as np

   # Load the structure
   p = PDBParser()
   structure = p.get_structure('X', pdb_file)

   # Get the coordinates of all the atoms
   coords = np.array([atom.get_coord() for atom in structure.get_atoms() if is_aa(atom.get_parent().get_resname())])

   # Calculate the center of mass
   center_of_mass = coords.mean(axis=0)

   # Calculate the radius of gyration
   rg = np.sqrt(((coords - center_of_mass)**2).sum(axis=1).mean())

   return rg