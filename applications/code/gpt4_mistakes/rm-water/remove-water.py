import os
import mdtraj as md 

traj = md.load(os.path.join(_FILE_DIR_,'trp-cage-small.trr'), top=os.path.join(_FILE_DIR_,'trp-cage.pdb'))
nowater = traj.remove_solvent()
result = True if remove_water(os.path.join(_FILE_DIR_,'trp-cage-small.trr'),os.path.join(_FILE_DIR_,'trp-cage.pdb')).n_atoms == nowater.n_atoms else False 