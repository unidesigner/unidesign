Implement a first draft of a "NeuroHDF" layout according to the principles
outlined in "Unifying Biological Image Formats with HDF5"
http://queue.acm.org/detail.cfm?id=1628215

There is the BioHDF initiative, with very similar goals. Their specification is here:
* http://www.hdfgroup.org/projects/biohdf/biohdf_documentation.html
* http://finchtalk.geospiza.com/2010/04/bloginar-standardizing-bioinformatics.html

Design Goals
------------
* Specify group layout convention
* Specify usage of attributes
* Unicode support?
* Self-documenting I/O format

Compatability/Export
--------------------
* NeuroML: http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000815
* NineML: http://www.nineml.org/news/news.shtml

Need to represent:
1) spiking neurons
2) synapses
3) populations of neurons and
4) connectivity patterns across populations of neurons.

Datastructures
--------------
Tree
http://en.wikipedia.org/wiki/Tree_%28data_structure%29
http://en.wikipedia.org/wiki/Binary_heap

3D Shape
* contour pile
* voxel enumeration
* triangulation of the surface
Methods for conversion between data types
3D BASE: A GEOMETRICAL DATA BASE SYSTEM FOR THE ANALYSIS AND VISUALISATION OF 3D-SHAPES OBTAINED
FROM PARALLEL SERIAL SECTIONS INCLUDING THREE DIFFERENT GEOMETRICAL REPRESENTATIONS
