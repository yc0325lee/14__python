#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__matplotlib_hist.py
# - author : yc0325lee
# - created : 2022-12-07 22:55:11 by yc032
# - modified : 2022-12-07 22:55:11 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path
import numpy as np
import matplotlib.pyplot as plt
import random
np.random.seed(19680801) # seed-ing

if False:
    # - matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None,
    #   cumulative=False, bottom=None, histtype='bar', align='mid',
    #   orientation='vertical', rwidth=None, log=False, color=None,
    #   label=None, stacked=False, *, data=None, **kwargs
    # )
    # ; compute and plot a histogram.
    x = 4 + np.random.normal(0, 1.5, 200)
    bins_ = np.arange(0.0, 7.51, 0.5)
    print('[dbg ] len(x)=', len(x), 'min=', min(x), 'max=', max(x), 'sigma=', np.mean(x))

    fig, ax = plt.subplots(figsize=(9,6))
    n, bins, patches = ax.hist(x, bins=bins_)

    xticks = list()
    for i, patch in enumerate(patches):
        xticks.append(patch.get_x() + patch.get_width()/2.0)

    ax.set( # set multiple properties at once
        xticks=xticks,
        title='histogram',
        xlabel='x',
        ylabel='count'
    )
    ax.grid(visible=True, linestyle='dotted') # '--'

    plt.tight_layout() # adjust the padding between and around subplots
    index = 0
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if True:
    # - matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None,
    #   cumulative=False, bottom=None, histtype='bar', align='mid',
    #   orientation='vertical', rwidth=None, log=False, color=None,
    #   label=None, stacked=False, *, data=None, **kwargs
    # )
    # ; compute and plot a histogram.
    #
    # - matplotlib.pyplot.text(x, y, string, fontdict=None, **kwargs)
    # ; add text to the axes.
    # ; horizontalalignment or ha : {'left', 'center', 'right'}
    # ; verticalalignment or va : {'bottom', 'baseline', 'center', 'center_baseline', 'top'}
    x = 4 + np.random.normal(0, 1.5, 200)

    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
            'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    fig, ax = plt.subplots(figsize=(9,6))
    n, bins, patches = ax.hist(x, linewidth=0.5, color=None,
            edgecolor='black', facecolor='green')
    print('[dbg ] n=', n, 'len=', len(n))
    print('[dbg ] bins=', bins, 'len=', len(bins))

    xticks = list()
    for i, patch in enumerate(patches):
        patch.set_color(colors[i])
        xticks.append(patch.get_x() + patch.get_width()/2.0)
        ax.text(
            patch.get_x() + patch.get_width()/2.0, # x
            patch.get_height(), # y
            '%d(%.1f%%)' % (n[i], n[i]/np.sum(n)*100.0),
            ha='center', va='bottom'
        )

    ax.set(
        # set multiple properties at once
        xticks=xticks,
        title='histogram',
        xlabel='x',
        ylabel='count'
    )
    ax.grid(visible=True, linestyle='dotted') # '--'

    plt.tight_layout() # adjust the padding between and around subplots
    index = 1
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()
