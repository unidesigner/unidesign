unidesign.spatial
=================

geometry of neural activity
computational neuroanatomy
microcircuitry
functional geometry
the geometry of activation
see Rodolf Llinas Hellers Lecture

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
* Fractal measures: http://www.frontiersin.org/neuroanatomy/10.3389/fnana.2011.00045/full#B9

* Algorithm to detect closeness between arbors (potential synapses) "Identifying, tabulating, and analyzing contacts between branched neuron morphologies"
  http://bluebrain.epfl.ch/files/content/sites/bluebrain/files/Scientific%20Publications/2008%20-%20%20Identifying,%20tabulating,%20and%20analyzing%20contacts%20between%20branched%20neuron%20morphologies.pdf
* Meshing of Skeletons: "A Neuron Membrane Mesh Representation for Visualization of Electrophysiological Simulations"
  http://www.computer.org/portal/web/csdl/doi/10.1109/TVCG.2011.55
* Axonal and dendritic branching strategies. Correlation between synapse location and branch points:
  http://www.frontiersin.org/neural_circuits/10.3389/neuro.04.018.2009/full
* Use PCA to find neuron symmetry axes
  http://glowingpython.blogspot.com/2011/07/principal-component-analysis-with-numpy.html?spref=tw
* Draw process diagram: http://www.sbgn.org/Main_Page
* Synaptic measures http://www.johanneshjorth.se/SynD/SynD.html
* Anatomy to dendrograms, and use Gromov-­‐Hausdorff distance	Calrlsson, G.and Memoli, F(2010) JMLR
* http://mit.edu/lrv/www/elegans/
* motifs: 1:00 http://www.archive.org/details/Redwood_Center_2006_11_07_Chklovskii
* http://www.scholarpedia.org/article/Neuron
* http://www.scholarpedia.org/article/Neuroanatomy
* V Braitenberg and A Schüz. Cortex: Statistics and Geometry of Neuronal Connectivity. Springer, Berlin, Germany, 1998

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
* cell type X responsible to make cell type Y tuned to F. X and Y relationship? spatial overlap, synaptic connectivity, temporal correlations
References
==========
* H.B.M. Uylings, A. Ruiz-Marcos, J. van Pelt, The metric analysis of three-dimensional dendritic tree patterns: a methodological review, Journal of Neuroscience Methods, Volume 18, Issues 1-2, October 1986, Pages 127-151, ISSN 0165-0270, DOI: 10.1016/0165-0270(86)90116-0.

What spatio-conceptual queries for visualization do you want to do?
- Show the skeleton and in-out connectivity with id X
- Show the arbor types (axon, dendrite, soma, pre, post) colored
- Show the axonal arbors of the complete spatial volume with different colors (depending on X)
- Show the dendrictic arbors ... "
- Show loop motifs...
- Show "excitatory"/"inhibitory" cells...
- Show connectors as sphere, colored by their type, radius scaled with their volume

Circuits
* http://www.igi.tugraz.at/
* http://www.lsm.tugraz.at/download/index.html

A personal view of the early development of computational neuroscience in the USA
require extensive, quantitative descriptions of neuronal properties:
(1) the ion channel types, their densities and their distributions throughout each neuron;
(2) the types and properties of intracellular calcium ion buffers, and their effect on intracellular
    spatial and temporal profiles of calcium concentration;
(3) neurotransmitters, their release mechanisms, and modulation of release by activity;
(4) neurotransmitter receptor types, properties, and sensitivity to modulation by other
    transmitters, hormones or activity; and
(5) intracellular chemical reactions and signaling pathways which may, in turn, affect the release of
    transmitters and the sensitivity of receptors