__author__ = 'sgerhard'

"""
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

See appendix of http://www.springerlink.com/content/37h5r777825292lv/fulltext.pdf
"""