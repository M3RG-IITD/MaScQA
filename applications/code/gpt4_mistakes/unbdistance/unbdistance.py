import mdtraj as md
import os
import math
import numpy as np


#_FILE_DIR_ = '.'
lig_str = 'TMP'
traj_path = os.path.join(_FILE_DIR_, 'traj.dcd') 
top_path = os.path.join(_FILE_DIR_, 'top.pdb')
traj = md.load(traj_path, top=top_path)
top = traj.topology
prot_idxs = top.select('protein')
lig_idxs = top.select(F'resname == {lig_str}')
traj2 = md.load(traj_path, atom_indices=prot_idxs, top=top_path)
traj3 = md.load(traj_path, atom_indices=lig_idxs, top=top_path)

dist = []
for i,j in zip(traj2,traj3):
    com_a = md.compute_center_of_mass(i)[0]
    com_b = md.compute_center_of_mass(j)[0]
    dist.append(((com_a[0]-com_b[0])**2+(com_a[1]-com_b[1])**2+(com_a[2]-com_b[2])**2)**0.5)

# assert

distances = unbdistance(traj,lig_str)

check = math.isclose(dist[0],distances[0])
check2 = math.isclose(dist[-1],distances[-1])
result = True if check and check2 else False 
