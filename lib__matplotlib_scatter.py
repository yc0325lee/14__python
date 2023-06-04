#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__matplotlib_scatter.py
# - author : yc0325lee
# - created : 2022-12-08 23:31:59 by yc032
# - modified : 2022-12-08 23:31:59 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
random.seed(19680801) # seed-ing

if True:
    # - matplotlib.pyplot.scatter(
    #       x, y, s=None, c=None, marker=None, cmap=None, norm=None,
    #       vmin=None, vmax=None, alpha=None, linewidths=None,
    #       *, edgecolors=None, plotnonfinite=False, data=None, **kwargs
    #   )
    # ; a scatter plot of y vs. x with varying marker size and/or color
    # ; s : the marker size in points**2 (typographic points are 1/72 inch)
    # ; c : array-like or list of colors or color
    xvals = np.random.rand(100)
    yvals = np.random.rand(100)
    sizes = np.sqrt(xvals**2 + yvals**2) * 1000.0
    colors = cm.rainbow(np.linspace(0.0, 1.0, len(yvals)))
    #iterator = itertools.cycle(['r', 'g', 'b'])
    #colors = [next(iterator) for _ in range(len(yvals))]

    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(xvals, yvals, s=sizes, c=colors, alpha=0.5)
    ax.set(
        title='scatter plot',
        xlabel='x',
        ylabel='y',
        xticks=np.arange(0.0, 1.01, 0.1),
        yticks=np.arange(0.0, 1.01, 0.1),
    )
    ax.grid(visible=True, linestyle='dotted') # '--'

    plt.tight_layout() # adjust the padding between and around subplots
    index = 0
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()
