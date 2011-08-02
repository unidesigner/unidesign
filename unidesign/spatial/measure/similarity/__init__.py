"""
Tree Comparison
---------------

* http://www.slideshare.net/hecfran/tree-distance-algorithm
* Klein. Computing the Edit-Distance Between Unrooted Ordered Trees
* http://useless-factor.blogspot.com/2008/01/matching-diffing-and-merging-xml.html
* Pattern Matching Book http://books.google.com/books?id=mFd_grFyiT4C

Entities on which comparison could be performed:
1. only tree topology
2. tree topology and spatial embeddedness
3. skeleton with axon/dendritic arbor and connectors (and their type)

Methods/Ideas:
* measure on teh entity and compare measure (factor analysis)
* tree edit distance
* invariants: scale, rotational, affine; symmetry exploration
* bounding volume comparison, convex hull
* network-based comparison
* sample in volumetric space and 3D cross-correlation
* define an evolutionary model and compare its parameters
* sphereness, tubeness, torusness

"""