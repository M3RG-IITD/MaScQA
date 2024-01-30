def sle(eqns):
   """
   This function solves a system of linear equations {['a_0x_0 + b_0x_1 = c0','a_1x_0 + b_1x_1 = c1']}.
   """
   import numpy as np
   a = np.array([[eqns[0][0], eqns[0][1]], [eqns[1][0], eqns[1][1]]])
   b = np.array([eqns[0][2], eqns[1][2]])
   x = np.linalg.solve(a, b)
   return x