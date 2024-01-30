def calc_rdbs(smiles):
     """
     Return degrees of unsaturation (Double Bond Equivalent) from C, N, H, Halogen count.
     """
     from rdkit import Chem
     mol = Chem.MolFromSmiles(smiles)
     c = 0
     n = 0
     h = 0
     hal = 0
     for atom in mol.GetAtoms():
         if atom.GetSymbol() == 'C':
             c += 1
         elif atom.GetSymbol() == 'N':
             n += 1
         elif atom.GetSymbol() == 'H':
             h += 1
         elif atom.GetSymbol() in ['F', 'Cl', 'Br', 'I']:
             hal += 1
     d = c - (h/2) + (n/2) + 1 - (hal/2)
     return d