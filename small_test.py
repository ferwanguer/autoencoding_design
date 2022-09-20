import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
import os

results_path = 'Results'
results = np.load(os.path.join(results_path,'mus_sigmas_02_second.npz'))
mus = results['mu']
sigmas = results['sigma']

print(mus)
cmap_list = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
x, y = np.mgrid[-3:3:.01, -3:3:.01]
pos = np.dstack((x, y))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
for i in range(11):
    rv = multivariate_normal(mus[i], np.diag(np.exp(sigmas[i])))
    ax2.contour(x, y, rv.pdf(pos), 100, cmap=cmap_list[i], alpha = 0.5)



plt.show()