#!/usr/bin/env python

# Code is from http://maxberggren.se/2015/08/04/basemap/

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap

m = Basemap(resolution='c',
            projection='kav7',
            lat_0=0.,  # Center around
            lon_0=0.)  # lat 0, lon 0

n_graticules = 18
parallels = np.arange(-80., 90, n_graticules)
meridians = np.arange(0., 360., n_graticules)
lw = 1
dashes = [5, 7]  # 5 dots, 7 spaces... repeat
graticules_color = 'grey'

fig1 = plt.figure(figsize=(16, 20))
fig1.patch.set_facecolor('#e6e8ec')
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])

m.drawmapboundary(color='white',
                  linewidth=0.0,
                  fill_color='white')
m.drawparallels(parallels,
                linewidth=lw,
                dashes=dashes,
                color=graticules_color)
m.drawmeridians(meridians,
                linewidth=lw,
                dashes=dashes,
                color=graticules_color)
m.drawcoastlines(linewidth=0)
m.fillcontinents('black',
                 lake_color='white')
m.drawcountries(linewidth=1,
                linestyle='solid',
                color='white',
                zorder=30)

title = plt.title('World map (Kavrayskiy 7)',
                  fontsize=20)
title.set_y(1.03)  # Move the title a bit for niceness
plt.savefig("map_example.png")
