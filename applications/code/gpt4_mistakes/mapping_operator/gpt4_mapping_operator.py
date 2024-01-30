def mapping_operator(molecule, beads_mappings):
   """
   This function generates a mass-mass weighted mapping matrix given an MD analysis molecule
   and atom selections for the beads.
   """
   M = np.zeros((len(molecule.atoms), len(beads_mappings)))
   for i, beads in enumerate(beads_mappings):
       for bead in beads:
           M[bead, i] = molecule.atoms[bead].mass
   M /= M.sum(axis=0)
   return M