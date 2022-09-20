import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
import os

results_path = 'Results'
results = np.load(os.path.join(results_path,'mus_sigmas.npz'))
mus = results['mu']
sigmas = results['sigma']



x, y = np.mgrid[-2:2:.01, -2:2:.01]
pos = np.dstack((x, y))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
for i in range(11):
    rv = multivariate_normal(mus[i], np.diag(np.exp(sigmas[i])))
    ax2.contourf(x, y, rv.pdf(pos), 100, cmap="Oranges", alpha = 0.05)



plt.show()