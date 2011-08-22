Required attributes
Recommended attributes:
Optional attributes:

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
---------
* ModelDB web site: http://senselab.med.yale.edu/modeldb
* NeuronDB web site: http://senselab.med.yale.edu/neurondb
* http://www.NeuroMorpho.Org
* http://mattions.github.com/neuronvisio/index.html
* SWC Databases http://krasnow.gmu.edu/cn3/L-Neuron/database/index.html
* http://research.mssm.edu/cnic/repository.html

Open Issues
===========

* Should the layout recommendation propose `level of detail representations <http://books.google.com/books?id=CB1N1aaoMloC&pg=PA9&lpg=PA9&dq=represent+levels+of+details&source=bl&ots=eaHOdD0-1j&sig=3Gp_ub9UAr94aBFHN3lzKkW_QNM&hl=en&ei=02f9Taa3Lsj50gHHq4iWAw&sa=X&oi=book_result&ct=result&resnum=8&ved=0CEIQ6AEwBw>`_?
* How to deal with missing slices?
* Is SliceSet efficient for thousands of slices?
* Check if nothing is missing from what is expressible in `FieldML/MeshML <http://www.physiome.org.nz/xml_languages/fieldml/documents/meshml_fieldml.html/>`_

