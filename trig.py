#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

x = np.arange(0, np.pi, 0.1)
y = np.sin(x)

# TODO fill in this function
def integrate(y, dx):
	return np.sum(y)*dx

print('Numercial approximation of integral of sin(x) from 0 to pi = {} \n'.format(integrate(y,0.1)))

plt.plot(x, y)
plt.show()

y_1 = np.cos(x)

I = quad(lambda x: np.cos(x), 0, np.pi)
I = I[0]
print('Numerical approximation of integral of cos(x) from 0 to pi = {} \n'.format(I))

plt.figure()
plt.plot(x, y_1)
plt.show()
