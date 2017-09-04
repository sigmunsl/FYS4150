import numpy as np
import time
import matplotlib.pyplot as plt
from matricies import trifactor, trisolve, tdma


n = 1000000
x = np.linspace(0, 1, n+1)
a = -1.
b = np.zeros(n+1)
c = -1.
d = 2.

for i in range(1, n+1):
    fx = 100*np.e**(-10*x[i])
    h = 1/(n+1)
    b[i] = h**2*fx

start = time.time()

v = tdma(a, b[1:n], c, d)
v = np.insert(v, 0, 0)
v = np.append(v, 0)

total_time = time.time()-start

print('Time: ' + str(total_time))

'''
plt.plot(x, v)
plt.xlabel(r"x")
plt.ylabel(r"v(x)")
plt.title(r'Velocity for v(x), $x\in(0,1)$ and n = ' + str(n))
plt.savefig('1b_n' + str(n) + '.pdf')
plt.show()
'''