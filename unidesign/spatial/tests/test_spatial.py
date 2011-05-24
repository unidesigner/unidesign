""" Test unidesign.spatial module """

from unidesign import spatial

from unidesign.spatial.geometry import Tree, Connector

from unidesign.spatial.container import Region, ConnectorSet

forest1 = Forrest()

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
length1 = spatial.measure.arbor_length( tree1 )

# e.g. a tree, i.e. its vertices could be labeled, e.g. 3 could mean dendrite
spatial.measure.arbor_length( tree1, selection_key = 'labeling', selection_value = '3')

# estimate the arbor volume
arborvol1 = spatial.measure.arbor_volume( tree1 )

# count the outgoing Connector for a Tree in a Region
spatial.query.outconnections_count( region1, tree1 )

# count the incoming Connector for a Tree in a Region
spatial.query.inconnections_count( region1, tree1 )

# Does a connection exist between two Tree objects? Returns boolean
spatial.query.connection_exists( region1, tree1, tree2 )

# Extract backbone of Tree interpreted as Graph
spatial.function.extract_backbone( tree1 )

# Convert a Tree to a Graph object
graph1 = spatial.function.convert_tree_to_graph( tree1 )

# Convert a directed, acycle graph to Tree
tree1_converted = spatial.function.convert_graph_to_tree( graph1 )

# Find shortest topological path between two objects in a region
spatial.function.shortest_topological_path( tree1, tree2 )
spatial.function.shortest_topological_path( connector1, connector2 )

# Also for spatial distances
spatial.function.shortest_spatial_path( connector1, connector2 )

# The similarity of two Tree objects (arborizations)
spatial.function.similarity( tree1, tree2, metric/method = '' )

# Closeness of the tree from a given point
spatial.function.spatial_distance( tree1, point1 )

# Reduce the number of vertices describing the geometry, but keep
# it as accurate as possible. Root/Branch/Leaf nodes might be more relevant
# (spline_filter?)
tree1_simplified = spatial.function.simplify( tree1, accuracy )

# Retrieve networkx graph for the connectivity in a region based-on different methods
# of defining the graph

# Retrieve all elements in a given Region from a given Region
# 3D Spatial selector can be: Box, Sphere, Cylinder, Cone
# also see: http://www.neuroconstruct.org/docs/regions.html
result_group = spatial.query.find_entities( in = region1, spatial_selector = region2 )
# Retrieve trees for a given spatial selector region: e.g. a box, sphere

# Extract network from a Region
# need to specify network connection:
# http://www.neuroconstruct.org/docs/Glossary_gen.html#Network%20Connection

# Returns Center-Of-Gravity / representative point
# Ensure that it is always clear for returned coordinates in what
# spatial reference frame they are, and what units
tree1.get_center_of_gravity() / .centroid
connector1.get_center_of_gravity() / .centroid

##############
# Associate Geometry with Semantics
##############

from unidesign.semantics.entities import Neuropile, Neuron, Synapse, Tract, Cell?
# wrapper classes to add semantically relevant attributes to geometric types
# class inheritance? can we say validly a Neuron is a Tree? It is rather: Tree is a model of a Neuron.
# But also other geometric "models" are possible, such as areatree, voxelsets, (labeled) contourstack etc.
# Rather introduce a 3DGeometry or 3DGeometryRegion object ?
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
unidesign.semantics.semantic_query( "" )
