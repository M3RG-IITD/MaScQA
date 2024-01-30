import numpy as np
mgs = matrix_generators(66)
ref = np.array([[1, 0, 0, 1/2],
                [0, 1, 0, 1/2],
                [0, 0, 1, 0]])
result = np.allclose(mgs[-1], ref)
