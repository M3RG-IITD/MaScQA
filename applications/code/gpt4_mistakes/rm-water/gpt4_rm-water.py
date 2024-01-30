def remove_water(traj_file,top_file):
   """
   This function removes solvent from loaded trajectory traj_file and topology in top_file to return the new trajctory
   """
   import mdtraj as md

   # Load the trajectory
   traj = md.load(traj_file, top=top_file)

   # Get the indices of the water molecules
   water_indices = traj.topology.select('water')

   # Remove the water molecules
   new_traj = traj.atom_slice(water_indices, inplace=False)

   return new_traj