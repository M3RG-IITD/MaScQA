def matrix_generators(gnum):
     """ Returns list of matrix generators for general positions of given space group
     gnum -  International Tables for Crystallography space group number
     """
     # Import necessary module
     from sympy import Matrix

     # Define the matrix generators for each space group
     matrix_generators_dict = {
         1: [Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])],
         2: [Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])],
         # Add more space groups as needed
     }

     # Get the matrix generators for the given space group
     generators = matrix_generators_dict.get(gnum, None)

     if generators is None:
         raise ValueError(f"No matrix generators defined for space group {gnum}")

     return generators