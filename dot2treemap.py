#! /usr/bin/env python

import argparse
import pygraphviz as pgv

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

parser = argparse.ArgumentParser(description='Render a dot tree as a treemap.')
parser.add_argument('filepath', help='A dot file')

args = parser.parse_args()

graph=pgv.AGraph(args.filepath)
print graph.__dict__
graph.layout() # layout with default (neato)
graph.draw('simple.png') # draw png
