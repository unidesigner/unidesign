""" Load Region from NeuroHDF and apply measures to retrieved trees """

from unidesign.spatial.group import Region, Treelines, Connectors
from neurohdf import File

f = File('mydataset.nh5', 'r')

# wrap a region
myregion = Region.from_neurohdf(f, 'neuropile')

# fetch cells
# level defines how many indirections: connectors, trees etc. to fetch into memory
# creating objects for trees and connectors
myregion.fetch( neuron_id, level = 0 )

# or fetch all
myregion.fetch_all()

# retrieve particular kinds of trees
myregion.retrieve( class = 'tree', where = 'type = sensory neuron', fetch = False )
myregion.retrieve( class = 'connector', fetch = False )

# produce a connectivity diagram from the currently fetched trees/connectors
# for multiple connectors between, a nx.MultiDiGraph might be used
connection_diagram = myregion.get_graph()

# produce a connectivity diagram for neuron classes
myregion.get_class_graph( include_classes = ['all'] )

# display the diagram

# usecase: color tree based on the centrality of treenodes
# 1) convert to graph
# 2) compute centrality
# 3) feed centrality into colormap
# 4) create fos actor with information

# =======

class Tree(object):

    points = None
    connectivity = None

    # concepts, fetched from NeuroHDF
    labels = None
    # ...
    # dynamically add using setattr and getattr

    # outgoing connectors
    output = []

    # incoming connectors
    input = []

    def reroot(self, new_root_id):
        # reroot a tree
        # take care, rerooting would might change the ids
        # and subsequently invalidate the connectors
        # no, it is just changing the connectivity
        pass
    
    def subtree(self, subtree_root_id, copy = True):
        # return a new tree with the given root subtree
        pass

    def attach(self, tree_instance, treenode_nodeid_to_merge_onto):
        # attach another tree to self at the given treenode id
        pass

    def split(self, at_treenode):
        # split Tree at treenode, returning two new trees
        # might be better defined somewhere else
        pass

class Connector(object):

    location = None

    # incoming connections
    input = []
    # outgoing connections
    output = []
