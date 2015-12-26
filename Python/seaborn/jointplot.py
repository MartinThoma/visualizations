#!/usr/bin/env python
import numpy as np
from scipy.stats import kendalltau
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)

plot = sns.jointplot(x, y, kind="hex", stat_func=kendalltau, color="#4CB391")
# plt.show()

import matplotlib
rcParams = matplotlib.rcParams
rcParams['svg.fonttype'] = 'none'  # No text as paths. Assume font installed.

rcParams['font.serif'] = ['Times New Roman']
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.family'] = 'sans-serif'
plt.savefig("jointplot.png")
