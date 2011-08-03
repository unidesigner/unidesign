unidesign.spatial
=================

Focus:
* Fiji/TrakEM https://github.com/acardona/Fiji-TrakEM2-scripts
* http://code.google.com/p/treestoolbox/
* http://www.treestoolbox.org/index.html

From Molecular Dynamics
=======================
http://pymol.org/
http://www2.molmovdb.org/wiki/info/index.php/Macromolecular_Geometry

======================

Geometer:http://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter
http://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter

http://paulbourke.net/geometry/
http://en.wikipedia.org/wiki/Spatial_query

For example, mapping of variables and geometry specs are things that will need to be worked out in order to do a proposed
ML for compartmental chemistry and compartmental neuronal modeling.

A common issue in multiscale models is the valuable capability of being able to switch between scales of representation.

Consider the case where a channel is spread over a dendrite. We want to provide a mapping between channel conductance
in each location , and the level of some molecule in the same location. Alternatively, we may want to deliver a stimulus
at a specific location along the deendrite, and so need to specify which receptor instances to activate.

Goal: want compartmental chemistry and compartmental neuronal modelling

The future models of axonal guidance will probably be similar to existent modelf of cell chemotaxis. (standard reaction-diffusion models)
Nomenclature
============
* tree, treeline, skeleton
* segment, section, line
* connector
* treenode, vertex, node
* positions, points, locations, vertices

Motivation
==========
* http://krasnow.gmu.edu/cn3/data-tools.html
* http://www.neuroconstruct.org/
* http://www.ucl.ac.uk/mrsic-flogel/MF_lab/Home.html
* http://neura.org/NeuRA_Homepage/Start.html
** http://home.earthlink.net/~perlewitz/sftwr.html#morphology
* https://github.com/tfoutz99/Neuron3D
* Figure 4 in http://www.ini.uzh.ch/~acardona/papers/Cardona_2010_lineage_identification.pdf

* Inspiration from imglib2 design
* http://geodjango.org/
* http://www.gdal.org/
* GeoSpatial community http://gispython.org/shapely/docs/1.0/manual.html#background
* http://www.neurogeometry.net/
* Numpy array tricks (e.g. amin) http://www.slideshare.net/enthought/numpy-talk-at-siam
* http://netmorph.org/
* Spatial hash function for collision detection: http://www.beosil.com/download/CollisionDetectionHashing_VMV03.pdf
* Synaptic World http://www.johanneshjorth.se/SynD/SynD.html

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
    * if global, want to extract one arborization (e.g. make it local), and then do analysis
* fiber bundle format: time slice at the topmost level. what is the most efficient? how far does it depend on the data and required operations?
* importance of the ability to select/deselect, group elements for easier interactivity
* backend storage using neurohdf or ORM and database, e.g. with sqlalchemy

References
==========
* H.B.M. Uylings, A. Ruiz-Marcos, J. van Pelt, The metric analysis of three-dimensional dendritic tree patterns: a methodological review, Journal of Neuroscience Methods, Volume 18, Issues 1-2, October 1986, Pages 127-151, ISSN 0165-0270, DOI: 10.1016/0165-0270(86)90116-0.

