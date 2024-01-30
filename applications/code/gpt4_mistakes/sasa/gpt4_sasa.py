def protein_surface_area(pdb_file):
   """
   1. This function loads a pdb
   2. Calculates the Solvent Accessible Surface Area (sasa) per residue
   3. Returns it
   """
   from Bio.PDB import PDBParser
   from Bio.PDB.DSSP import DSSP

   # Load the pdb file
   p = PDBParser()
   structure = p.get_structure('X', pdb_file)

   # Calculate the sasa per residue
   model = structure[0]
   dssp = DSSP(model, pdb_file)
   sasa = [residue[3] for residue in dssp]

   return sasa