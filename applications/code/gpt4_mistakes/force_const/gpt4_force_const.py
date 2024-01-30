def compute_k(m1,m2,wave_len):
     """
     Two atom harmonic oscillator.
     Returns force constant in kg/s**2 units given masses m1,m2 and wave length
     wave_len. Masses are in kg units and wave length in cm^-1 units. Use reduced mass.
     """
     # Convert wave length from cm^-1 to m^-1
     wave_len_m = wave_len * 100

     # Calculate reduced mass
     reduced_mass = (m1 * m2) / (m1 + m2)

     # Calculate force constant
     k = (2 * 3.14159 * wave_len_m)**2 * reduced_mass

     return k