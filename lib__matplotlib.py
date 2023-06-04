#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__matplotlib.py
# - author : yc0325lee
# - created : 2022-12-04 19:48:06 by yc032
# - modified : 2022-12-04 19:48:06 by yc032
# - description : 
# - references
# ; https://www.analyticsvidhya.com/blog/2020/05/10-matplotlib-tricks-data-visualization-python/
# - matplotlib.pyplot
# ; matplotlib.pyplot is a state-based interface to matplotlib. It provides an
#   implicit, MATLAB-like, way of plotting. It also opens figures on your
#   screen, and acts as the figure GUI manager.
# ; https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot
#   -> see 'plotting commands'
# ; writing mathematical expressions
#   -> https://matplotlib.org/stable/tutorials/text/mathtext.html
# ----------------------------------------------------------------------------
import os, os.path
import numpy as np
import matplotlib.pyplot as plt
import time
import random
np.random.seed(19680801) # seed-ing

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #1 – how to change plot size?
    # - matplotlib.pyplot.figure(
    #       num=None, figsize=None, dpi=None, *, facecolor=None,
    #       edgecolor=None, frameon=True,
    #       FigureClass=<class 'matplotlib.figure.Figure'>,
    #       clear=False, **kwargs
    #   )
    # ; create a new figure, or activate an existing figure.
    # ; figsize=(width, height)
    # - matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
    # ; plot y versus x as lines and/or markers.
    # - matplotlib.pyplot.savefig(*args, **kwargs)
    # ; filename
    # ; format = png(default), pdf, svg, ...
    # ; bbox_inches
    #   bounding box in inches: only the given portion of the figure is saved.
    #   if 'tight', try to figure out the tight bbox of the figure.
    #
    # - matplotlib.pyplot.grid(visible=None, which='major', axis='both', **kwargs)
    # ; configure the grid lines.
    # ; which - 'major', 'minor', 'both'
    # ; axis - 'x', 'x', 'both'
    #
    # - matplotlib.pyplot.show(*, block=None)
    # ; display all open figures.
    #
    # - matplotlib.pyplot.xlabel(
    #       xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs
    #   )
    # ; set the label for the x-axis
    # ; fontsize=10
    #
    # - matplotlib.pyplot.ylabel(
    #       ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs
    #   )
    # ; set the label for the y-axis.
    # ------------------------------------------------------------------------
    xvals = list(range(0, 100))
    yvals = [x + x*random.random() for x in xvals]

    fig = plt.figure(figsize=(8,4)) # default: [6.4, 4.8]
                                    # plt.rcParams["figure.figsize"]
    plt.plot(xvals, yvals)
    plt.title('line plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(linestyle='--')
    plt.tight_layout() # adjust the padding between and around subplots
    index = 0
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #2 – how to generate subplots? (1)
    # - matplotlib.pyplot.subplot(*args, **kwargs)
    # ; add an axes to the current figure or retrieve an existing axes.
    # ; signatures
    #   subplot(nrows, ncols, idx, **kwargs)
    #   subplot(pos, **kwargs)
    #   subplot(**kwargs)
    #   subplot(ax)
    # ; idx starts from 1
    # ------------------------------------------------------------------------
    xvals = list(range(0, 100))
    yvals1 = [x + x*random.random() for x in xvals]
    yvals2 = [x - x*random.random() for x in xvals]

    fig = plt.figure(figsize=(16,4))

    ax1 = plt.subplot(1, 2, 1) # (1)
    ax1.plot(xvals, yvals1)
    ax1.set_title('plot 1')
    ax1.grid(linestyle='dotted')

    ax2 = plt.subplot(1, 2, 2) # (2)
    ax2.plot(xvals, yvals2)
    ax2.set_title('plot 2')
    ax2.grid(linestyle='dotted')

    plt.tight_layout()
    index = 1
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #2 – how to generate subplots? (2)
    #
    # - matplotlib.pyplot.subplots(
    #       nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True,
    #       width_ratios=None, height_ratios=None, subplot_kw=None,
    #       gridspec_kw=None, **fig_kw
    #   )
    # ; create a figure and a set of subplots.
    # ; returns (fig, axes) tuple
    # ; convenient to create common layouts of subplots, including the
    #   enclosing figure object, in a single call.
    # ; all the plots are of the same size
    #
    # - subplots_adjust(
    #       left=None, bottom=None, right=None, top=None,
    #       wspace=None, hspace=None
    #   )
    # ; adjust the subplot layout parameters.
    xvals = list(range(0, 100))
    yvals1 = [x + x*random.random() for x in xvals]
    yvals2 = [x - x*random.random() for x in xvals]
    yvals3 = [x + x*random.random() for x in xvals]
    yvals4 = [x - x*random.random() for x in xvals]

    fig, axes = plt.subplots(2, 2, figsize=(16,8)) # 2x2
    #                        |  |
    #                        |  ncols
    #                        nrows

    axes[0][0].plot(xvals, yvals1) # ax #1
    axes[0][0].set_title('plot 1')
    axes[0][0].grid(linestyle='dotted') # '--'

    axes[0][1].plot(xvals, yvals1) # ax #2
    axes[0][1].set_title('plot 2')
    axes[0][1].grid(linestyle='dotted') # '--'

    axes[1][0].plot(xvals, yvals2) # ax #3
    axes[1][0].set_title('plot 3')
    axes[1][0].grid(linestyle='dotted') # '--'

    axes[1][1].plot(xvals, yvals3) # ax #4
    axes[1][1].set_title('plot 4')
    axes[1][1].grid(linestyle='dotted') # '--'

    #print('[dbg ] axes=', axes)
    # [dbg ] axes= [
    #   [<AxesSubplot: title={'center': 'plot 1'}>
    #    <AxesSubplot: title={'center': 'plot 2'}>]
    #   [<AxesSubplot: title={'center': 'plot 3'}>
    #    <AxesSubplot: title={'center': 'plot 4'}>]
    # ]

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 2
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #2 – how to generate subplots? (3)
    # - matplotlib.pyplot.subplot2grid(
    #       shape, loc, rowspan=1, colspan=1, fig=None, **kwargs
    #   )
    # ; create a subplot at a specific location inside a regular grid.
    # ; returns the axes of the subplot
    # ; shape(int, int)
    #   number of rows and of columns of the grid in which to place axis
    # ; loc(int, int)
    #   row number and column number of the axis location within the grid
    # ; rowspanint, default: 1
    #   number of rows for the axis to span downwards
    # ; colspanint, default: 1
    #   number of columns for the axis to span to the right
    xvals = list(range(0, 100))
    yvals1 = [x + x*random.random() for x in xvals]
    yvals2 = [x - x*random.random() for x in xvals]
    yvals3 = [x + x*random.random() for x in xvals]
    yvals4 = [x - x*random.random() for x in xvals]

    fig = plt.figure(figsize=(8,8))

    ax1 = plt.subplot2grid((4,4), (0,0), colspan=3) # rowspan=1(default) -> 3x1
    ax1.plot(xvals, yvals1)
    ax1.set_title('plot 1 : (0,0)')
    ax1.grid(linestyle='dotted') # '--'

    ax2 = plt.subplot2grid((4,4), (0,3), colspan=1) # rowspan=1(default) -> 1x1
    ax2.plot(xvals, yvals2)
    ax2.set_title('plot 2 : (0,3)')
    ax2.grid(linestyle='dotted') # '--'

    ax3 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=3) # 3x3
    ax3.plot(xvals, yvals3)
    ax3.set_title('Plot 3 : (1,0)')
    ax3.grid(linestyle='dotted') # '--'

    ax4 = plt.subplot2grid((4,4), (1,3), rowspan=3, colspan=1) # 1x3
    ax4.plot(xvals, yvals4)
    ax4.set_title('plot 4 : (1,3)')
    ax4.grid(linestyle='dotted') # '--'

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 3
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #3 – how to annotate plots? (1)
    # - annotation
    # ; annotation is a comment added to a plot at a point for making it more
    #   understandable.
    # - functions
    #   text()
    #   annotate()
    #
    # - matplotlib.pyplot.bar(
    #       x, height, width=0.8, bottom=None, *, align='center', data=None,
    #       **kwargs
    #   )
    # ; make a bar plot.
    # ; x - x coordinates of the bars
    #
    # - matplotlib.pyplot.xticks(ticks=None, labels=None, *, minor=False, **kwargs)
    # ; get or set the current tick locations and labels of the x-axis
    #
    # - matplotlib.pyplot.text(x, y, string, fontdict=None, **kwargs)
    # ; add text to the axes.
    # ; horizontalalignment or ha : {'left', 'center', 'right'}
    # ; verticalalignment or va : {'bottom', 'baseline', 'center', 'center_baseline', 'top'}
    cities = ['City A','City B','City C','City D','City E']
    temps = [random.uniform(20, 40) for i in range(len(cities))]
    x_pos = list(range(1,6)) # [1, 2, 3, 4, 5]

    fig = plt.figure(figsize=(6,6))
    graph = plt.bar(x_pos, temps, color='violet')

    plt.title('city temperature')
    plt.xticks(x_pos, cities)
    plt.xlabel('cities')
    plt.ylabel('temperature ($^\circ$C)')

    for bar, t in zip(graph, temps):
        plt.text(
            bar.get_x() + bar.get_width()/2.0, # center
            bar.get_height(),
            '%.2f $^\circ$C' % t,
            ha='center', # horizontal alignment
            va='bottom' # vertical alignment
        )

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 4
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #3 – how to annotate plots? (2)
    # - matplotlib.pyplot.annotate(text, xy, xytext=None, xycoords='data',
    #       textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)
    # ; annotate the point xy with text text.
    # ; arrowprops : dict, optional
    #   the properties used to draw a fancyarrowpatch arrow between the
    #   positions xy and xytext.
    xvals = np.arange(10, dtype=np.float32)
    yvals = np.exp(xvals)

    fig = plt.figure(figsize=(8,6))

    plt.plot(xvals, yvals)
    plt.title('annotating exponential plot using plt.annotate()')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    plt.annotate('point 1', xy=(6,400), arrowprops=dict(arrowstyle='->'), xytext=(4,600))
    plt.annotate('point 2', xy=(7,1150), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.2'), xytext=(4.5,2000))
    plt.annotate('point 3', xy=(8,3000), arrowprops=dict(arrowstyle='-|>', connectionstyle='angle,angleA=90,angleB=0'), xytext=(8.5,2200))

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 5
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #4 – how to modify the limit of axes? (1)
    xvals = np.arange(10, dtype=np.float32)
    yvals = np.exp(xvals)

    fig = plt.figure(figsize=(8,6))

    plt.plot(xvals, yvals)
    plt.title('changing limits of x and y using xlim()/ylim()')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # changing axes limits
    plt.ylim(1.0, 8000)
    plt.xlim(0.0, 9.0)

    # removing axes from the figure

    plt.annotate('point 1', xy=(6,400), arrowprops=dict(arrowstyle='->'), xytext=(4,600))
    plt.annotate('point 2', xy=(7,1150), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.2'), xytext=(4.5,2000))
    plt.annotate('point 3', xy=(8,3000), arrowprops=dict(arrowstyle='-|>', connectionstyle='angle,angleA=90,angleB=0'), xytext=(8.5,2200))

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 6
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #4 – how to modify the limit of axes? (2)
    # - matplotlib.pyplot.gca()
    # ; get the current axes
    xvals = np.arange(10, dtype=np.float32)
    yvals = np.exp(xvals)

    fig = plt.figure(figsize=(8,6))

    plt.plot(xvals, yvals)
    plt.title('top/right spines removed')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # changing axes limits
    plt.ylim(1.0, 8000)
    plt.xlim(0.0, 9.0)

    # removing axes from the figure
    # ; top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.annotate('point 1', xy=(6,400), arrowprops=dict(arrowstyle='->'), xytext=(4,600))
    plt.annotate('point 2', xy=(7,1150), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.2'), xytext=(4.5,2000))
    plt.annotate('point 3', xy=(8,3000), arrowprops=dict(arrowstyle='-|>', connectionstyle='angle,angleA=90,angleB=0'), xytext=(8.5,2200))

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 7
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #4 – how to modify the limit of axes? (3)
    # - setting the color of the spines manually using the set_color() function
    xvals = np.arange(10, dtype=np.float32)
    yvals = np.exp(xvals)

    fig = plt.figure(figsize=(8,6))

    plt.plot(xvals, yvals)
    plt.title('top/right spines removed')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    # changing axes limits
    plt.ylim(1.0, 8000)
    plt.xlim(0.0, 9.0)

    # removing axes from the figure
    # ; top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    #changing color of the axes
    plt.gca().spines['left'].set_color('red')
    plt.gca().spines['bottom'].set_color('green')

    plt.annotate('point 1', xy=(6,400), arrowprops=dict(arrowstyle='->'), xytext=(4,600))
    plt.annotate('point 2', xy=(7,1150), arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.2'), xytext=(4.5,2000))
    plt.annotate('point 3', xy=(8,3000), arrowprops=dict(arrowstyle='-|>', connectionstyle='angle,angleA=90,angleB=0'), xytext=(8.5,2200))

    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 8
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #5 – how to make plots interactive?
    # - use jupyter notebook
    pass

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #6 – how to group bar plots?
    # - overlapping 2 bar charts
    # - matplotlib.pyplot.bar(
    #       x, height, width=0.8, bottom=None, *, align='center', data=None,
    #       **kwargs
    #   )
    cities = ['City A','City B','City C','City D','City E']
    temps_summer = [random.uniform(20, 40) for i in range(len(cities))]
    temps_winter = [random.uniform(0, 10) for i in range(len(cities))]
    x_pos_summer = list(range(1,6)) # [1, 2, 3, 4, 5]
    x_pos_winter = [x+0.4 for x in x_pos_summer] # [1.4, 2.4, 3.4, 4.4, 5.4]

    fig = plt.figure(figsize=(10,6))
    graph_summer = plt.bar(
        x_pos_summer, temps_summer, color='tomato', label='summer', width=0.4)
    graph_winter = plt.bar(
        x_pos_winter, temps_winter, color='dodgerblue', label='winter', width=0.4)

    plt.title('city temperature')
    plt.xticks([x+0.2 for x in x_pos_summer], cities)
    plt.xlabel('cities')
    plt.ylabel('temperature ($^\circ$C)')

    # bars : bar_summer
    # barw : bar_winter
    # ts : text_summer
    # tw : text_winter
    for bars, barw, ts, tw in zip(graph_summer, graph_winter, temps_summer, temps_winter):
        plt.text(bars.get_x() + bars.get_width()/2.0, bars.get_height(),
            '%.2f$^\circ$C' % ts, ha='center', va='bottom') # summer
        plt.text(barw.get_x() + barw.get_width()/2.0, barw.get_height(),
            '%.2f$^\circ$C' % tw, ha='center', va='bottom') # winter

    plt.legend()
    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 9
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #7 – how to modify ticks?
    # - modifying ticks using xticks() and yticks()
    # - matplotlib.pyplot.xticks(ticks=None, labels=None, *, minor=False, **kwargs)
    # ; get or set the current tick locations and labels of the x-axis.
    cities = ['City A','City B','City C','City D','City E']
    temps_summer = [random.uniform(20, 40) for i in range(len(cities))]
    temps_winter = [random.uniform(0, 10) for i in range(len(cities))]
    x_pos_summer = list(range(1,6)) # [1, 2, 3, 4, 5]
    x_pos_winter = [x+0.4 for x in x_pos_summer] # [1.4, 2.4, 3.4, 4.4, 5.4]

    fig = plt.figure(figsize=(10,6))
    graph_summer = plt.bar(
        x_pos_summer, temps_summer, color='tomato', label='summer', width=0.4)
    graph_winter = plt.bar(
        x_pos_winter, temps_winter, color='dodgerblue', label='winter', width=0.4)

    plt.title('city temperature')

    # removing axes from the figure - top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.xticks([x+0.2 for x in x_pos_summer], cities,
        fontname='monospace', rotation=45, fontsize=8
    )
    plt.xlabel('cities', fontsize=14)
    plt.ylabel('temperature ($^\circ$C)', fontsize=14)

    # bars : bar_summer
    # barw : bar_winter
    # ts : text_summer
    # tw : text_winter
    for bars, barw, ts, tw in zip(graph_summer, graph_winter, temps_summer, temps_winter):
        plt.text(bars.get_x() + bars.get_width()/2.0, bars.get_height(),
            '%.2f$^\circ$C' % ts, ha='center', va='bottom') # summer
        plt.text(barw.get_x() + barw.get_width()/2.0, barw.get_height(),
            '%.2f$^\circ$C' % tw, ha='center', va='bottom') # winter

    plt.legend()
    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 10
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #8 – how to modify legends?
    # - matplotlib.pyplot.legend(*args, **kwargs)
    # ; place a legend on the axes
    # ; loc - location of legend, default='best'
    cities = ['City A','City B','City C','City D','City E']
    temps_summer = [random.uniform(20, 40) for i in range(len(cities))]
    temps_winter = [random.uniform(0, 10) for i in range(len(cities))]
    x_pos_summer = list(range(1,6)) # [1, 2, 3, 4, 5]
    x_pos_winter = [x+0.4 for x in x_pos_summer] # [1.4, 2.4, 3.4, 4.4, 5.4]

    fig = plt.figure(figsize=(10,6))
    graph_summer = plt.bar(
        x_pos_summer, temps_summer, color='tomato', label='summer', width=0.4)
    graph_winter = plt.bar(
        x_pos_winter, temps_winter, color='dodgerblue', label='winter', width=0.4)

    plt.title('city temperature')

    # removing axes from the figure - top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.xticks([x+0.2 for x in x_pos_summer], cities,
        fontname='monospace', rotation=45, fontsize=8
    )
    plt.xlabel('cities', fontsize=14)
    plt.ylabel('temperature ($^\circ$C)', fontsize=14)

    # bars : bar_summer
    # barw : bar_winter
    # ts : text_summer
    # tw : text_winter
    for bars, barw, ts, tw in zip(graph_summer, graph_winter, temps_summer, temps_winter):
        plt.text(bars.get_x() + bars.get_width()/2.0, bars.get_height(),
            '%.2f$^\circ$C' % ts, ha='center', va='bottom') # summer
        plt.text(barw.get_x() + barw.get_width()/2.0, barw.get_height(),
            '%.2f$^\circ$C' % tw, ha='center', va='bottom') # winter

    # modifying legend
    #plt.legend() # default
    plt.legend(loc='upper center', ncol=2, frameon=False)
    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 11
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #9 – how to add watermarks? (1)
    # - using text()
    # - matplotlib.pyplot.text(x, y, string, fontdict=None, **kwargs)
    # ; add text to the axes.
    # ; horizontalalignment or ha : {'left', 'center', 'right'}
    # ; verticalalignment or va : {'bottom', 'baseline', 'center', 'center_baseline', 'top'}
    cities = ['City A','City B','City C','City D','City E']
    temps_summer = [random.uniform(20, 40) for i in range(len(cities))]
    temps_winter = [random.uniform(0, 10) for i in range(len(cities))]
    x_pos_summer = list(range(1,6)) # [1, 2, 3, 4, 5]
    x_pos_winter = [x+0.4 for x in x_pos_summer] # [1.4, 2.4, 3.4, 4.4, 5.4]

    fig = plt.figure(figsize=(10,6))
    graph_summer = plt.bar(
        x_pos_summer, temps_summer, color='tomato', label='summer', width=0.4)
    graph_winter = plt.bar(
        x_pos_winter, temps_winter, color='dodgerblue', label='winter', width=0.4)

    plt.title('city temperature')

    # removing axes from the figure - top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.xticks([x+0.2 for x in x_pos_summer], cities,
        fontname='monospace', rotation=45, fontsize=8
    )
    plt.xlabel('cities', fontsize=14)
    plt.ylabel('temperature ($^\circ$C)', fontsize=14)

    # bars : bar_summer
    # barw : bar_winter
    # ts : text_summer
    # tw : text_winter
    for bars, barw, ts, tw in zip(graph_summer, graph_winter, temps_summer, temps_winter):
        plt.text(bars.get_x() + bars.get_width()/2.0, bars.get_height(),
            '%.2f$^\circ$C' % ts, ha='center', va='bottom') # summer
        plt.text(barw.get_x() + barw.get_width()/2.0, barw.get_height(),
            '%.2f$^\circ$C' % tw, ha='center', va='bottom') # winter

    # text watermark
    fig.text(
        0.85, 0.15, 'Analytics Vidhya',
        fontsize=65, color='gray', ha='right', va='bottom',
        alpha=0.4,rotation=25
    )

    # modifying legend
    #plt.legend() # default
    plt.legend(loc='upper center', ncol=2, frameon=False)
    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 12
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # ------------------------------------------------------------------------
    # matplotlib trick #9 – how to add watermarks? (2)
    # - adding watermark image using the figimage() function
    # - figimage(
    #       X, xo=0, yo=0, alpha=None, norm=None, cmap=None, vmin=None,
    #       vmax=None, origin=None, resize=False, **kwargs
    #   )
    # ; add a non-resampled image to the figure.
    # ; xo, yo - int, the x/y image offset in pixels
    # ; resize=False
    #   if true, resize the figure to match the given image size.
    cities = ['City A','City B','City C','City D','City E']
    temps_summer = [random.uniform(20, 40) for i in range(len(cities))]
    temps_winter = [random.uniform(0, 10) for i in range(len(cities))]
    x_pos_summer = list(range(1,6)) # [1, 2, 3, 4, 5]
    x_pos_winter = [x+0.4 for x in x_pos_summer] # [1.4, 2.4, 3.4, 4.4, 5.4]

    fig = plt.figure(figsize=(10,6))
    graph_summer = plt.bar(
        x_pos_summer, temps_summer, color='tomato', label='summer', width=0.4)
    graph_winter = plt.bar(
        x_pos_winter, temps_winter, color='dodgerblue', label='winter', width=0.4)

    plt.title('city temperature')

    # removing axes from the figure - top/bottom/left/right
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.xticks([x+0.2 for x in x_pos_summer], cities,
        fontname='monospace', rotation=45, fontsize=8
    )
    plt.xlabel('cities', fontsize=14)
    plt.ylabel('temperature ($^\circ$C)', fontsize=14)

    # bars : bar_summer
    # barw : bar_winter
    # ts : text_summer
    # tw : text_winter
    for bars, barw, ts, tw in zip(graph_summer, graph_winter, temps_summer, temps_winter):
        plt.text(bars.get_x() + bars.get_width()/2.0, bars.get_height(),
            '%.2f$^\circ$C' % ts, ha='center', va='bottom') # summer
        plt.text(barw.get_x() + barw.get_width()/2.0, barw.get_height(),
            '%.2f$^\circ$C' % tw, ha='center', va='bottom') # winter

    # image watermark
    import matplotlib.image as img
    logo = img.imread(fname='yclee.png')
    fig.figimage(logo, 100, 70, alpha=0.3)

    # modifying legend
    #plt.legend() # default
    plt.legend(loc='upper center', ncol=2, frameon=False)
    plt.tight_layout()
    plt.grid(linestyle='dotted') # or '--'
    index = 13
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # (1) using current axes concept
    # ; multiple plt.subplot() used
    # ; plt.subplot() changes current ax
    # - 
    data = np.random.randn(2, 100) # shape=(2,100), mean=0.0, variance=1.0
    x = np.arange(100)

    fig = plt.figure(figsize=(10, 5))
    
    # axs[0,0]
    plt.subplot(2, 2, 1) # axs[0,0]
    n, bins, patches = plt.hist(data[0])
    plt.title("hist()")
    plt.xlabel("data[0]")
    plt.ylabel("frequency")
    plt.grid()

    # axs[0,1]
    plt.subplot(2, 2, 2) # axs[0,1]
    plt.plot(x, data[1])
    plt.title("plot()")
    plt.xlabel("x")
    plt.ylabel("data[1]")
    plt.grid()

    # axs[1,0]
    plt.subplot(2, 2, 3) # axs[1,0]
    plt.scatter(data[0], data[1])
    plt.title("scatter()")
    plt.xlabel("data[0]")
    plt.ylabel("data[1]")
    plt.grid()

    # axs[1,1]
    plt.subplot(2, 2, 4) # axs[1,1]
    plt.hist2d(data[0], data[1])
    plt.title("hist2d()")
    plt.xlabel("data[0]")
    plt.ylabel("data[1]")
    plt.grid()

    plt.tight_layout() # adjust the padding between and around subplots
    index = 14
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # (2) OO-syle plotting
    # ; plt.subplots() used
    data = np.random.randn(2, 100)
    x = np.arange(100)

    #fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5))
    fig, axs = plt.subplots(2, 2, figsize=(10, 5)) # default figsize=(6.4, 4.8)

    # axs[0,0]
    axs[0,0].hist(data[0])
    axs[0,0].set_title("hist()")
    axs[0,0].set_xlabel("data[0]")
    axs[0,0].set_ylabel("frequency")
    axs[0,0].grid(visible=True, which='both', axis='both')

    # axs[0,1]
    axs[0,1].plot(x, data[1])
    axs[0,1].set_title("plot()")
    axs[0,1].set_xlabel("x")
    axs[0,1].set_ylabel("data[1]")
    axs[0,1].grid()

    # axs[1,0]
    axs[1,0].scatter(data[0], data[1])
    axs[1,0].set_title("scatter()")
    axs[1,0].set_xlabel("data[0]")
    axs[1,0].set_ylabel("data[1]")
    axs[1,0].grid()

    # axs[1,1]
    axs[1,1].hist2d(data[0], data[1])
    axs[1,1].set_title("hist2d()")
    axs[1,1].set_xlabel("data[0]")
    axs[1,1].set_ylabel("data[1]")
    axs[1,1].grid()

    plt.tight_layout() # adjust the padding between and around subplots
    index = 15
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # using subplots() and ax objects
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))
    fig.suptitle('A tale of 2 subplots')
    
    ax1.plot(x1, y1, 'o-')
    ax1.set_ylabel('damped oscillation')
    ax1.grid()
    
    ax2.plot(x2, y2, '.-')
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('undamped')
    ax2.grid()
    
    plt.tight_layout() # adjust the padding between and around subplots
    index = 16
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()


if False:
    # using just subplot() and current ax
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    fig = plt.figure(figsize=(10, 5))
    
    plt.subplot(2, 1, 1) # ax1
    plt.plot(x1, y1, '-r')
    plt.title('a tale of 2 subplots')
    plt.ylabel('damped oscillation')
    plt.grid()
    
    plt.subplot(2, 1, 2) # ax2
    plt.plot(x2, y2, '-g')
    plt.xlabel('time (s)')
    plt.ylabel('undamped')
    plt.grid()
    
    plt.tight_layout() # adjust the padding between and around subplots
    index = 17
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # 3d wireframe plot
    x_ = np.arange(-30, 30, 1)
    y_ = np.arange(-30, 30, 1)
    x, y = np.meshgrid(x_, y_)
    z = x**2 + y**2
    #print(x.shape) # (60, 60)
    #print(y.shape) # (60, 60)
    #print(z.shape) # (60, 60)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # plot a basic wireframe.
    ax.plot_wireframe(x, y, z, rstride=4, cstride=4)
    plt.tight_layout() # adjust the padding between and around subplots
    index = 18
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    x_ = np.arange(-5, 5, 0.15)
    y_ = np.arange(-5, 5, 0.15)
    x, y = np.meshgrid(x_, y_)
    r = np.sqrt(x**2 + y**2)
    z = np.sin(r)
    #print("x=", x.shape); print(x)
    #print("y=", y.shape); print(y)
    #print("r=", r.shape); print(r)
    #print("z=", z.shape); print(z)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis')
    ax.set_title("plot_surface()")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x,y)')
    ax.set_xlim([-5.1, 5.1])
    ax.set_ylim([-5.1, 5.1])

    plt.tight_layout() # adjust the padding between and around subplots
    index = 19
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # - matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None,
    #   cumulative=False, bottom=None, histtype='bar', align='mid',
    #   orientation='vertical', rwidth=None, log=False, color=None,
    #   label=None, stacked=False, *, data=None, **kwargs
    # )
    # ; compute and plot a histogram.
    x = 4 + np.random.normal(0, 1.5, 200)
    bins = np.arange(0.0, 7.1, 0.5)
    #print('x=', x, len(x))

    #fig = plt.figure(figsize=(4,4)) # default: [6.4, 4.8]
                                    # plt.rcParams["figure.figsize"]
    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(x, bins=bins, linewidth=0.5, edgecolor="white")
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(0.0, 7.51, 0.5),
        ylim=(0, 35),
        yticks=np.linspace(0, 35, 6),
        title='histogram',
        xlabel='x',
        ylabel='count'
    )
    ax.grid()

    plt.tight_layout() # adjust the padding between and around subplots
    index = 20
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()

if False:
    # - matplotlib.pyplot.axis(*args, emit=True, **kwargs)
    # ; convenience method to get or set some axis properties.
    # ; pyplot.axis([xmin, xmax, ymin, ymax])
    pass

if True:
    # - matplotlib.pyplot.matshow(A, fignum=None, **kwargs)
    # ; display an array as a matrix in a new figure window
    # ; visualizes a 2D matrix or array as color-coded image
    confusion_matrix = [
        [ 915,    1,   11,    3,    3,   15,    7,    0,   13,    0],
        [   0, 1037,    9,    9,    0,   13,    2,    4,   28,    2],
        [   5,    9,  875,   18,   19,   11,   24,   12,   44,    5],
        [  10,    2,   22,  828,    2,   50,    5,   10,   45,   15],
        [   2,    1,   18,    2,  903,    2,   13,    7,   23,   40],
        [  12,    4,    7,   46,   15,  745,   17,    3,   52,   18],
        [   5,    8,   16,    2,   11,   17,  923,    0,   11,    1],
        [   3,    2,   16,    4,    9,    6,    0,  960,    8,   38],
        [   6,   15,   10,   20,    3,   30,    9,    2,  881,   16],
        [   3,    1,    8,   15,   19,   10,    0,   41,   34,  824],
    ]

    fig = plt.figure(figsize=(8,8)) # default: [6.4, 4.8]
                                    # plt.rcParams["figure.figsize"]
    plt.matshow(confusion_matrix, cmap=plt.cm.gray)
    #plt.tight_layout() # adjust the padding between and around subplots
    index = 21
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()
    fig.clear()

    row_sums = np.sum(confusion_matrix, axis=1, keepdims=True) # (10, 1)
    normalized = confusion_matrix / row_sums
    print(normalized)
    # [[0.94524793 0.00103306 0.01136364 0.00309917 0.00309917 0.01549587 0.00723140 0.00000000 0.01342975 0.00000000]
    #  [0.00000000 0.93931159 0.00815217 0.00815217 0.00000000 0.01177536 0.00181159 0.00362319 0.02536232 0.00181159]
    #  [0.00489237 0.00880626 0.85616438 0.01761252 0.01859100 0.01076321 0.02348337 0.01174168 0.04305284 0.00489237]
    #  [0.01011122 0.00202224 0.02224469 0.83720930 0.00202224 0.05055612 0.00505561 0.01011122 0.04550051 0.01516684]
    #  [0.00197824 0.00098912 0.01780415 0.00197824 0.89317507 0.00197824 0.01285856 0.00692384 0.02274975 0.03956479]
    #  [0.01305767 0.00435256 0.00761697 0.05005441 0.01632209 0.81066376 0.01849837 0.00326442 0.05658324 0.01958651]
    #  [0.00503018 0.00804829 0.01609658 0.00201207 0.01106640 0.01710262 0.92857143 0.00000000 0.01106640 0.00100604]
    #  [0.00286807 0.00191205 0.01529637 0.00382409 0.00860421 0.00573614 0.00000000 0.91778203 0.00764818 0.03632887]
    #  [0.00604839 0.01512097 0.01008065 0.02016129 0.00302419 0.03024194 0.00907258 0.00201613 0.88810484 0.01612903]
    #  [0.00314136 0.00104712 0.00837696 0.01570681 0.01989529 0.01047120 0.00000000 0.04293194 0.03560209 0.86282723]]

    np.fill_diagonal(normalized, 0.0)
    plt.matshow(normalized, cmap=plt.cm.gray)
    index = 22
    filename = os.path.splitext(os.path.basename(__file__))[0] + '-{:02d}.png'.format(index)
    print('[info] saving image to {} ...'.format(filename))
    plt.savefig(filename, bbox_inches="tight")
    #plt.show()
    plt.close()
    fig.clear()
