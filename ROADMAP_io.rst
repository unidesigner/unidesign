Implement a first draft of a "NeuroHDF" layout according to the principles
outlined in "Unifying Biological Image Formats with HDF5"
http://queue.acm.org/detail.cfm?id=1628215

There is the BioHDF initiative, with very similar goals. Their specification is here:
* http://www.hdfgroup.org/projects/biohdf/biohdf_documentation.html
* http://finchtalk.geospiza.com/2010/04/bloginar-standardizing-bioinformatics.html

HDF5 forum
* http://hdf-forum.184993.n3.nabble.com/

Design Goals
------------
* Propose the hierarchical layout with groups and datasets,
  only later define a set of core characteristics for
  a valid standard
* Specify group layout convention
* Specify usage of attributes
* Unicode support?
* Self-documenting I/O format

Compatability/Export
--------------------
* NeuroML: http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000815
* NineML: http://www.nineml.org/news/news.shtml
* Learn from Bioinf community: http://abhishek-tiwari.com/2009/02/comparison-of-cellml-and-sbml.html

Interfacing with Simulation Environments
----------------------------------------
Based on the review "Computer Simulation Environments" by Gleeson et al.

* NEURON
    * section object for cable modelling? section = (line) segment?
    * Import/Export in NeuroML format
* GENESIS
    * OO elements that communicate with each other (about 130 objects)
* NEST
    * See connectivity specification

Resources
* ModelDB web site: http://senselab.med.yale.edu/modeldb
* NeuronDB web site: http://senselab.med.yale.edu/neurondb
* http://www.NeuroMorpho.Org
* http://mattions.github.com/neuronvisio/index.html
* SWC Databases http://krasnow.gmu.edu/cn3/L-Neuron/database/index.html

Datastructures
--------------
Tree
http://en.wikipedia.org/wiki/Tree_%28data_structure%29
http://en.wikipedia.org/wiki/Binary_heap

Need to represent:
1) spiking neurons -> NineML?
2) synapses -> connectors
3) populations of neurons and -> region with trees and connectors
4) connectivity patterns across populations of neurons, or classes of neurons