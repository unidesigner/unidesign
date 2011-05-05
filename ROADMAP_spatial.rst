unidesign.spatial
=================

unidesign.spatial.measurement
-----------------------------
Finds the distance between points, polygon area, etc.

unidesign.spatial.geometry
--------------------------
How to accomodate different data structures?

unidesign.spatial.geometry.basic

.point
.line
.rectangle
.circle
.sphere
.polygon
.area
.vector

(derive from pyeuclid)

unidesign.spatial.geometry.advanced

.tree
.connector

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

unidesign.spatial.query / .predicates
-----------------------
Spatial Predicates: Allows true/false queries such as 'is there a residence located within a mile of the area we are planning to build the landfill?'

unidesign.spatial.region
------------------------
* needs a spatial reference frame (origo, coordinate axes, units)
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

Design Goals
============
* Keep it simple. (Reduction of the conceptual complexity affords adoption)
* Keep it open to interface. (Embedd in the software ecosystem: simulators, visualization, ontologies, internet, (molecular biology)
* Design towards modular hierarchical structure, toward multi-scale. (Components are themselves complex entities with their own internal dynamics.)
* Keep the temporal domain in mind.
* Design toward collaborative process of exploration
* Scalable data analysis capabilities
* "Thin" classes to underlying data from NeuroHDF