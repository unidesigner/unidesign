"""
unidesign.spatial.geometry.advanced
-----------------------------------

.tree vs. skeleton (skeltonization)
methods:
- delete_treenode, and rejoin
- reroot
- add_node_with_parent
- add_node_on_segment

.spine

.connector
attributes: spatial location, inslot, outslot, type

(e.g. tree - spine - connector - tree )

.areatree, also see skeletonization

Other 3D Shape
* contour pile
* voxel enumeration
* triangulation of the surface
Methods for conversion between data types
3D BASE: A GEOMETRICAL DATA BASE SYSTEM FOR THE ANALYSIS AND VISUALISATION OF 3D-SHAPES OBTAINED
FROM PARALLEL SERIAL SECTIONS INCLUDING THREE DIFFERENT GEOMETRICAL REPRESENTATIONS
"""



class Tree(object):

    vertices = None
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

    # Reduce
    # reduce tree and keep only branching vertices

class Connector(object):

    location = None

    # incoming connections
    input = []
    # outgoing connections
    output = []
