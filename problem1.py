import scipy as sp
import numpy as np

# \frac{\sin\theta + 1}{\cos\theta}R + \ln\left(1 - \frac{R}{\cos\theta}\right) = 0 \\

theta = np.pi / 4
func = lambda R: (np.sin(theta) + 1) / np.cos(theta) * R + np.log(1 - R / np.cos(theta))

# Root finding using scipy's fsolve
R_solution = sp.optimize.fsolve(func, 0.5)
print(f"The range of the projectile is: {R_solution[0]}")