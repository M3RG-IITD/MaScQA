import math
import numpy as np

h2o_smiles = "O"
a = 0.61094
b = 17.635
c = 243.04
T = 25

exp_1 = ((b*T)/(T+c))
exp_2 = math.exp(exp_1)
vp_calc = a*exp_2


result = np.isclose(vapor_pressure("O"), vp_calc) 
