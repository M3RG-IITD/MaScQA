def get_ca_indices(pdb_file):
   """
   This function uploads a pdb file and find out the indices of first two alpha carbon atoms.
   """
   with open(pdb_file, 'r') as file:
       lines = file.readlines()

   idx = []
   for i, line in enumerate(lines):
       if line.startswith('ATOM'):
           elements = line.split()
           if elements[2] == 'CA':
               idx.append(i)
               if len(idx) == 2:
                   break
   return idx