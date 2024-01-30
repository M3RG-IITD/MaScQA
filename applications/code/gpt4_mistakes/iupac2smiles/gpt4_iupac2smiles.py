def iupac2smiles(IUPAC):
     """
     This function takes in the IUPAC name string and converts it to a SMILES string
     """
     from rdkit import Chem
     from rdkit.Chem import AllChem
     mol = Chem.MolFromIUPACName(IUPAC)
     SMILES = Chem.MolToSmiles(mol)
     return SMILES