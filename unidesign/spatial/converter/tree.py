from numpy import vstack
from networkx import Graph

def convert_local_tree_topology_to_graph(loc_tree_topo, tree_node_labeling):
    """ Creates a directed, acyclic NetworkX graph from a local tree topology

    Parameters
    ----------
    loc_tree_topo: array-like
        The local tree toplogy, where the root node element is -1

    tree_node_labeling: array-like
        The integer ids for each tree node

    Returns
    -------
    G : NetworkX graph

    """

    assert( loc_tree_topo[0] == -1 )

    G = Graph()
    G.add_nodes_from( tree_node_labeling )
    # build up graph connectivity
    con = vstack( (loc_tree_topo, range(len(loc_tree_topo))) )
    # prune root node connectivity
    con = con[:,1:]
    # update with correct labels
    con = tree_node_labeling[con]
    G.add_edges_from( zip(con[0,:], con[1,:]) )

    return G
