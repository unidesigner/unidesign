"""
Defines (morphological) measures for different geometries
Finds the distance between points, polygon area, etc.

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
* head and neck diametersNumber of stems attached to the soma.
* position on the dendritic backbone
* shape classification (thin, mushroom, stubby)
* density and distribution on the tree

See appendix of http://www.springerlink.com/content/37h5r777825292lv/fulltext.pdf

http://online.itp.ucsb.edu/online/neuro10/stevens/rm/flashtv.html
http://online.itp.ucsb.edu/online/colloq/stevens1/

vs. general:
* arbor density function (for 2d and 3d)
"""

""" L-measure

* L-Measure: a web-accessible tool for the analysis, comparison and search of digital reconstructions of neuronal morphologies
* http://farsight-toolkit.org/wiki/L_Measure_functions
* http://cng.gmu.edu:8080/Lm/help/index.htm

Global parameters
-----------------
Topological
* Number of branches
* Number of terminal tips of tree
* Number of arbors attached to the soma

Spatial
* Total branch/path length
* Branch angles min/max/mean/std
* Dimension height/width/depth (bounding box)
* Surface area of soma
* Surface area of arbor (across all segments)
* Total volume of arborisation

Active Zones, Clusters

"""

