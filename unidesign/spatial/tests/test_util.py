""" Test `unidesign`.`spatial`.`util` module """

import numpy as np

from ..util import convert_local_tree_topology_to_graph

# all_top[np.where(all_lab == 2513)[0]]
# loc_tree_topo = array([-1,  3,  3,  0], dtype=int32)

# all_id[np.where(all_lab == 2513)[0]]
# tree_node_labeling = array([2515, 2519, 2521, 2517], dtype=int32)

# create a graph using the label ids as node id

def test_convert_tree_graph():

    loc_tree_topo = np.array([-1,  3,  3,  0], dtype=np.int32)
    tree_node_labeling = np.array([2515, 2519, 2521, 2517], dtype=np.int32)

    graph = convert_local_tree_topology_to_graph(loc_tree_topo, tree_node_labeling)

