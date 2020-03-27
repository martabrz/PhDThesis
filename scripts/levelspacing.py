import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0, 5, 100)

def wigner_dyson(s):
    return (32*np.power(s,2)/np.power(np.pi, 2))*np.exp(-4*np.power(s,2)/np.pi)

def poisson(s):
    return np.exp(-s)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(s, wigner_dyson(s), 'k-')
ax.plot(s, poisson(s), 'r-')
ax.set_xlabel('s')
ax.set_ylabel('P(s)')
fig.savefig('wd_p_dist.png', transparent = False, dpi = 400, bbox_inches = 'tight')
plt.close(fig)
