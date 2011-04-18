""" Test chora.spatial module """

from chora.geometry import Tree, Connector
from chora.container import Region, ConnectorSet

tree1 = Tree()
tree2 = Tree()
tree3 = Tree()

connector1 = Connector()
connector2 = Connector()

# Differing characteristics
# Group: grouping in a set of entities. A Group might have slots and can act as a node
# Region: a region might be embedded in a well-defined spatial/temporal coordinate system
region1 = Region() / Group()

connectorset1 = ConnectorSet()
connectorset1.add( [connector1, connector2] )

region1.add( tree1 )
region1.add( [tree2, tree3] )
region1.add( connectorset1 )

# length of the summed arborization with unit
length1 = chora.measure.arbor_length( tree1 )

# estimate the arbor volume
arborvol1 = chora.measure.arbor_volume( tree1 )

# count the outgoing Connector for a Tree in a Region
chora.query.outlinks_count( region1, tree1 )

# count the incoming Connector for a Tree in a Region
chora.query.inlinks_count( region1, tree1 )

# Does a connection exist between two Tree objects? Returns boolean
chora.query.is_links( region1, tree1, tree2 )

# Extract backbone of Tree interpreted as Graph
chora.function.extract_backbone( tree1 )

# Convert a Tree to a Graph object
graph1 = chora.function.convert_tree_to_graph( tree1 )

# Convert a directed, acycle graph to Tree
tree1_converted = chora.function.convert_graph_to_tree( graph1 )

# Find shortest topological path between two objects in a region
chora.function.shortest_topological_path( tree1, tree2 )
chora.function.shortest_topological_path( connector1, connector2 )
# Also for spatial distances
chora.function.shortest_spatial_path( connector1, connector2 )

# The similarity of two Tree objects (arborizations)
chora.function.similarity( tree1, tree2, metric/method = '' )

# Reduce the number of vertices describing the geometry, but keep
# it as accurate as possible. Root/Branch/Leaf nodes might be more relevant
# (spline_filter?)
tree1_simplified = chora.function.simplify( tree1, accuracy )

# Retrieve all elements in a given Region from a given Region
# 3D Spatial selector can be: Box, Sphere, Cylinder, Cone
# also see: http://www.neuroconstruct.org/docs/regions.html
result_group = chora.query.find_entities( in = region1, spatial_selector = region2 )

# Extract network from a Region
# need to specify network connection:
# http://www.neuroconstruct.org/docs/Glossary_gen.html#Network%20Connection

# Returns Center-Of-Gravity / representative point
# Ensure that it is always clear for returned coordinates in what
# spatial reference frame they are, and what units
tree1.get_center_of_gravity() / .centroid
connector1.get_center_of_gravity() / .centroid

from chora.semantics.entities import Neuropile, Neuron, Synapse, Tract, Cell?
# wrapper classes to add semantically relevant attributes to geometric types
neuron1 = Neuron( tree1 )
neuron2 = Neuron( tree2 )
neuron3 = Neuron( tree3 )
synapse1 = Synapse( connector1 )

# ALTERNATIVE: specify with relationship
tree1.model_of = Neuron()
connector1.model_of = Synapse( attr1 = ..., attr2 = ... )
tree1.add_spatial_model( Mesh, VolumeROI, ... )

# Initialization of a region as Neuropile would map all
# Tree as Neuron ? / Connector as Synapse ? Cannot automatically decide!
neuropile1 = Neuropile( region1 )

neuron1.celltype / .
synapse1.shape / .area / .mediating_NT / .density

# Maybe SPARQL syntax
chora.semantics.semantic_query( "" )
