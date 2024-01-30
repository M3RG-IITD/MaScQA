def unbdistance(traj,lig_str):
     """
     This function returns a list of distances between center of mass of
     protein and center of mass of lig_str in every frame of trajectory
     traj
 
     traj is an mdtraj trajectory object
     lig_str is a string with the residue name of the ligand
     """
     ligand = traj.topology.select('resname {}'.format(lig_str))
     protein = traj.topology.select('protein')
     result = mdtraj.compute_center_of_mass(traj.atom_slice(protein)) - mdtraj.compute_center_of_mass(traj.atom_slice(ligand))
     return result