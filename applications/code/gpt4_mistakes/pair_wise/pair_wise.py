import numpy as np
import sys
import os

pdb_file = os.path.join(_FILE_DIR_, "1VII.pdb")


def pairwise(pdb_file):
    import mdtraj as md
    from itertools import combinations
    pdb = md.load(pdb_file)
    cas = pdb.top.select("name CA")
    distances = []
    comb = combinations(cas, 2)
    distances = md.compute_distances(pdb, comb, periodic=True)
    return distances


my_result = pairwise(pdb_file)
nlcc_result = pairwise_dist(pdb_file)

#print("My result:", my_result)
#print("nlcc result", nlcc_result)

result = True if np.abs(np.mean(my_result) -
                        np.mean(nlcc_result)) < 0.01 else False
