import numpy as np

m1 = 12.0 #amu
m2 = 16.0 #amu
wave_len = 2100 #1/cm
mass_fac = 1.677e-27 #kg/amu
velocity = 2.99e10 #cm/s
pi = np.pi

mu = (m1*m2)/(m1+m2)*mass_fac 
omega = 2*pi*wave_len*velocity 
force_const = mu*omega**2

force_const_codex = compute_k(m1,m2,wave_len)

if np.isclose(force_const, force_const_codex) ==  True:
    result = True
else:
    result = False
