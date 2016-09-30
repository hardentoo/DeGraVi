import os

import matplotlib
matplotlib.use('cairo')

from graph import dependency_graph, tree_graph
from plotting import circular_depgraph
from utils import (
	GENTOO_PURPLE,
	GENTOO_PURPLE_A75,
	GENTOO_PURPLE_A50,
	GENTOO_PURPLE_LIGHT,
	GENTOO_PURPLE_LIGHT2,
	GENTOO_PURPLE_LIGHT2_A75,
	GENTOO_PURPLE_GREY,
	GENTOO_PURPLE_GREY_A75,
	GENTOO_PURPLE_GREY_A50,
	GENTOO_GREEN,
	GENTOO_GREEN_A75,
	)

#relative paths
thisscriptspath = os.path.dirname(os.path.realpath(__file__))
neurogentoo_file = os.path.join(thisscriptspath,"neurogentoo.txt")
NEUROGENTOO = [line.strip() for line in open(neurogentoo_file, 'r')]

def neurogentoo_graph():
	g = dependency_graph(['/usr/local/portage/neurogentoo'],
		overlay_colors=[GENTOO_PURPLE_LIGHT],
		overlay_text_colors=[GENTOO_PURPLE],
		overlay_edge_colors=[GENTOO_PURPLE_A50],
		extraneous_colors=[GENTOO_PURPLE_GREY],
		extraneous_text_colors=[GENTOO_PURPLE_GREY],
		highlight=NEUROGENTOO,
		highlight_color=GENTOO_GREEN,
		highlight_edge_color=GENTOO_GREEN_A75,
		textcolor=GENTOO_PURPLE,
		only_overlay=False,
		)
	circular_depgraph(g,
	save_as="~/ng.pdf"
	)

def neurogentoo_full_graph():
	g = dependency_graph(['/usr/portage','/usr/local/portage/neurogentoo'],
		overlay_colors=[GENTOO_PURPLE_GREY,GENTOO_PURPLE_LIGHT2],
		overlay_text_colors=[GENTOO_PURPLE_GREY,GENTOO_PURPLE],
		overlay_edge_colors=[GENTOO_PURPLE_GREY_A50,GENTOO_PURPLE_LIGHT2_A75],
		highlight=NEUROGENTOO,
		highlight_color=GENTOO_GREEN,
		highlight_edge_color=GENTOO_GREEN_A75,
		textcolor=GENTOO_PURPLE,
		)
	circular_depgraph(g,
	save_as="~/lg.pdf"
	)

def dep_tree():
	g = tree_graph(['/usr/portage'], NEUROGENTOO, highlight_overlays=["/usr/local/portage/neurogentoo"],
		seed_color=GENTOO_GREEN,
		seed_text_color=GENTOO_GREEN,
		seed_edge_color=GENTOO_GREEN_A75,
		highlight_color=GENTOO_PURPLE_LIGHT2,
		highlight_text_color=GENTOO_PURPLE,
		highlight_edge_color=GENTOO_PURPLE_LIGHT2_A75,
		base_color=GENTOO_PURPLE_GREY,
		base_text_color=GENTOO_PURPLE,
		base_edge_color=GENTOO_PURPLE_GREY_A50,
		)
	circular_depgraph(g,
	save_as="~/tg.pdf"
	)

if __name__ == '__main__':
	dep_tree()
	# neurogentoo_full_graph()
	neurogentoo_graph()
