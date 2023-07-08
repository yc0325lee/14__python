#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: ft=python ts=4 sw=4 tw=78 expandtab
# ----------------------------------------------------------------------------
# - file : lib__graphviz.py
# - author : yc0325lee
# - created : 2023-07-08 17:44:37 by yc032
# - modified : 2023-07-08 17:44:37 by yc032
# - description : 
# ----------------------------------------------------------------------------
import os, os.path, sys
import pprint
import argparse
import random
import re
import csv
import pickle
import graphviz

if False:
    # -------------------------------------
    # - graphviz.Graph(
    #       name=None, comment=None, filename=None, directory=None,
    #       format=None, engine=None, encoding='utf-8', graph_attr=None,
    #       node_attr=None, edge_attr=None, body=None, strict=False, *,
    #       renderer=None, formatter=None
    #   )
    # ; undirected graph
    #
    # - graphviz.Digraph(
    #       name=None, comment=None, filename=None, directory=None,
    #       format=None, engine=None, encoding='utf-8', graph_attr=None,
    #       node_attr=None, edge_attr=None, body=None, strict=False, *,
    #       renderer=None, formatter=None
    #   )
    # ; directed graph
    # ; graph_attr – mapping of (attribute, value) pairs for the graph.
    # ; node_attr – mapping of (attribute, value) pairs set for all nodes.
    # ; edge_attr – mapping of (attribute, value) pairs set for all edges.
    #
    # - node(name, label=None, _attributes=None, **attrs)
    # ; create a node.
    #
    # - edge(tail_name, head_name, label=None, _attributes=None, **attrs)
    # ; 
    #
    # - edges(iterable)
    # ; create a bunch of edges
    # ; iterable of (tail, head) pairs
    #
    # - render(
    #       filename=None, directory=None, view=False, cleanup=False,
    #       format=None, renderer=None, formatter=None, neato_no_op=None,
    #       quiet=False, quiet_view=False, *, outfile=None, engine=None,
    #       raise_if_result_exists=False, overwrite_source=False
    # )
    # ; save the source to file and render with the graphviz engine.
    # ; 
    pass



if False:
    # -------------------------------------
    # - unflatten vs staggered
    wide = graphviz.Digraph('wide')
    wide.edges(('0', str(i)) for i in range(1, 10))
    #print(wide.source)
    index = 0
    filename = os.path.basename(__file__) + '-{:02d}'.format(index)
    print(f'[info] writing {filename}.png ...')
    wide.render(filename=filename, format='png', cleanup=True, view=False)

    stagger_2 = wide.unflatten(stagger=2)
    index = 1
    filename = os.path.basename(__file__) + '-{:02d}'.format(index)
    print(f'[info] writing {filename}.png ...')
    stagger_2.render(filename=filename, format='png', cleanup=True, view=False)

    stagger_3 = wide.unflatten(stagger=3)
    index = 2
    filename = os.path.basename(__file__) + '-{:02d}'.format(index)
    print(f'[info] writing {filename}.png ...')
    stagger_3.render(filename=filename, format='png', cleanup=True, view=False)


if False:
    # -------------------------------------
    # - struct
    graph = graphviz.Digraph(name='Meridian', graph_attr={'rankdir':'LR'}, node_attr={'shape':'record'})
    graph.node('RuleBase', '<f0>RuleBase|<f1>field')

    graph.node('SinglePathRule', '<f0>SinglePathRule|<f1>field')
    graph.node('MultiPathRule', '<f0>MultiPathRule|<f1>field')
    graph.edge('RuleBase', 'SinglePathRule')
    graph.edge('RuleBase', 'MultiPathRule')

    line = 'CNTL DATA W_CNTL W_DATA'
    for rulename in line.split():
        graph.node(f'{rulename}', f'<f0>{rulename}|<f1>field')
        graph.edge('SinglePathRule', rulename)

    line = 'W_GLITCH W_G_CLK_GLITCH W_RECON_GROUPS InterfaceBase'
    for rulename in line.split():
        graph.node(f'{rulename}', f'<f0>{rulename}|<f1>field')
        graph.edge('MultiPathRule', rulename)

    line = 'INTERFACE U_INTERFACE W_INTERFACE'
    for rulename in line.split():
        graph.node(f'{rulename}', f'<f0>{rulename}|<f1>field')
        graph.edge('InterfaceBase', rulename)

    index = 3
    filename = os.path.basename(__file__) + '-{:02d}'.format(index)
    print(f'[info] writing {filename}.png ...')
    graph.render(filename=filename, format='png', cleanup=True, view=False)


if False:
    # -------------------------------------
    # - using existing dot-file
    # ; render(
    #       filename=None, directory=None, view=False, cleanup=False,
    #       format=None, renderer=None, formatter=None, neato_no_op=None,
    #       quiet=False, quiet_view=False, *, outfile=None, engine=None,
    #       raise_if_result_exists=False, overwrite_source=False
    #   )
    #   engine (str) – Layout engine for rendering ('dot', 'neato', …).
    #   format (Optional[str]) – Output format for rendering ('pdf', 'png', …). Can be omitted if an outfile with a known format is given, i.e. if outfile ends with a known .{format} suffix.
    #   filepath (Union[PathLike, str, None]) – Path to the DOT source file to render. Can be omitted if outfile is given, in which case it defaults to outfile.with_suffix('.gv').
    #   renderer (Optional[str]) – Output renderer ('cairo', 'gd', …).
    #   formatter (Optional[str]) – Output formatter ('cairo', 'gd', …).
    #   neato_no_op (Union[bool, int, None]) – Neato layout engine no-op flag.
    #   quiet (bool) – Suppress stderr output from the layout subprocess.
    #   outfile (Union[PathLike, str, None]) – Path for the rendered output file.
    #   raise_if_result_exits – Raise graphviz.FileExistsError if the result file exists.
    #   overwrite_filepath (bool) – Allow dot to write to the file it reads from. Incompatible with raise_if_result_exists.
    index = 3
    filename = os.path.basename(__file__) + '-{:02d}'.format(index)
    print(f'[info] writing {filename} ...')
    #graphviz.render('dot', 'png', filename)
    graphviz.render(engine='dot', format='png', filepath=filename)
