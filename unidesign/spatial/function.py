"""
unidesign.spatial.function
--------------------------
Modify existing features to create new ones, for example by providing a buffer around them, intersecting features, etc.
They are specific to the object types

Maybe there is some overlap with an spatial.edit subpackage

.tree
* concatenate(tree1, tree1joinnode, tree2, tree2joinnode)
* resample(tree, method)
* split(tree, treesplitnode)

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

Comparison of morphologies, tree metrics (used in DIADEM, tree edit distance):
http://www.springerlink.com/content/n77666586741q811/fulltext.pdf

"""