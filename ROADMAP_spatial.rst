unidesign.spatial
=================

unidesign.spatial.measure
-----------------------------
Finds the distance between points, polygon area, etc.

Defines (morphological) measures for different geometries

.tree
.tree.arbor
* total length (implies information about metric)
* diameter (along segement, or at start/endpoints)
* number of spines
* spine density
* mean spine length
* relative populations of spines of each class
* number of branch points

.tree.branchpoint
* angle of "child" segements

.tree.spine
* basis dimension: shape and size
* length
* volume (e.g. based on voxel)
* head and neck diameters
* position on the dendritic backbone
* shape classification (thin, mushroom, stubby)
* density and distribution on the tree



unidesign.spatial.geometry
--------------------------
How to accomodate different data structures?

.region


unidesign.spatial.geometry.basic
--------------------------------

.point
.line
.rectangle
.circle
.sphere / .ball
* x,y,z,radius,color

.polygon
.area
.vector

(derive from pyeuclid)

unidesign.spatial.geometry.advanced
-----------------------------------

.tree

.spine

.connector
attributes: spatial location, inslot, outslot, type

(e.g. tree - spine - connector - tree )

.areatree


unidesign.spatial.generator
---------------------------
(Statistical) generators of spatial geometry derived from small sets of parameters

* e.g. L-Neuron
* NETMORPH http://www.ncbi.nlm.nih.gov/pubmed/19672726 http://netmorph.org/

unidesign.spatial.function
--------------------------
Modify existing features to create new ones, for example by providing a buffer around them, intersecting features, etc.

Function prototype: functionName (parameter(s)) : return type
* Distance(geometry, geometry) : number
* Equals(geometry, geometry) : boolean
* Disjoint(geometry, geometry) : boolean
* Intersects(geometry, geometry) : boolean
* Touches(geometry, geometry) : boolean
* Crosses(geometry, geometry) : boolean
* Overlaps(geometry, geometry) : boolean
* Contains(geometry, geometry) : boolean
* Length(geometry) : number
* Area(geometry) : number
* Centroid(geometry) : geometry

Boolean operations:
* selection can be defined as a boolean operation/intersection
The voxel representation is most favourable representation for these types of operations

Numerical analysis: Depending much on the representation
e.g. voxel-related, tree-related, slice-related or surface-related measures

unidesign.spatial.converter
---------------------------

* from contour model to voxel model
    * Rasterization algorithms: http://en.wikipedia.org/wiki/Digital_Differential_Analyzer_%28graphics_algorithm%29
      e.g. Bresenham http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

* from voxel model to contour model

* from contour model to triangulation model

* from tree to graph

* from directed acyclic graph to tree

unidesign.spatial.query / .predicates
-----------------------
Spatial Predicates: Allows true/false queries such as 'is there a residence located within a mile of the area we are planning to build the landfill?'

unidesign.spatial.region
------------------------
* needs a spatial reference frame (origo, coordinate axes, units, spatial grid)
* can have a spatial data structure
* can contain geometry objects

Markup Language for Representing Vector Geometry Objects
http://en.wikipedia.org/wiki/Well-known_text

Concepts of space in Greek thought
http://books.google.com/books?id=4TyvpvBLz14C

http://paulbourke.net/geometry/
http://en.wikipedia.org/wiki/Spatial_query

Possible synapse metadata information/structure:
http://www.frontiersin.org/Cellular%20Neuroscience/specialtopics/building_up_the_inhibitory_syn/126

Motivation
==========
* http://krasnow.gmu.edu/cn3/data-tools.html
* http://www.neuroconstruct.org/
* http://www.ucl.ac.uk/mrsic-flogel/MF_lab/Home.html
* http://neura.org/NeuRA_Homepage/Start.html
* http://www.treestoolbox.org/index.html
* http://home.earthlink.net/~perlewitz/sftwr.html#morphology
* https://github.com/tfoutz99/Neuron3D
* BioHDF-XML-RDF http://abhishek-tiwari.com/2009/03/biohdf-xml-rdf-triplet.html
* http://en.wikipedia.org/wiki/DEVS
* Inspiration from imglib2 design
* Python Neo: http://packages.python.org/neo/classes.html (see RecordingPoint for link to spatial)
* Fiji/TrakEM

SWC Databases
-------------
* http://krasnow.gmu.edu/cn3/L-Neuron/database/index.html

Design Goals
============
* Keep it simple. (Reduction of the conceptual complexity affords adoption)
* Keep it open to interface. (Embedd in the software ecosystem: simulators, visualization, ontologies, internet, (molecular biology)
* Design towards modular hierarchical structure, toward multi-scale. (Components are themselves complex entities with their own internal dynamics.)
* Keep the temporal domain in mind.
* Design toward collaborative process of exploration
* Scalable data analysis capabilities
* "Thin" classes to underlying data from NeuroHDF
* Analogy (Desktop Publishing): The paper (the Region), the objects (Tree, ...), groups of objects, operations on groups of objects

Basic Questions
===============
* Storage of circuitry local (with individual self-contained elements) or global (as a big array with labels for indexing)
    * this questions are pertaining to: the data format, the data object model, the visualization object model


References
==========
* H.B.M. Uylings, A. Ruiz-Marcos, J. van Pelt, The metric analysis of three-dimensional dendritic tree patterns: a methodological review, Journal of Neuroscience Methods, Volume 18, Issues 1-2, October 1986, Pages 127-151, ISSN 0165-0270, DOI: 10.1016/0165-0270(86)90116-0.

