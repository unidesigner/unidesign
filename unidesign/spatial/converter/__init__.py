"""
unidesign.spatial.converter
---------------------------

* from contour model to voxel model
    * Rasterization algorithms: http://en.wikipedia.org/wiki/Digital_Differential_Analyzer_%28graphics_algorithm%29
      e.g. Bresenham http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

* from voxel model to contour model

* from contour model to triangulation model

* from tree to graph

* from directed acyclic graph to tree

* from SWC to tree, loading as a classmethod or into io?

Morphology converter, lots of SWC for testing
* http://neuronland.org/NLMorphologyConverter/NLMorphologyConverter.html


From contour to mesh
--------------------
3dbar by Piotr Majka

The most straightforward and at the same time lightweight solution to
process your slices into volume in my opinion is to:

1.Save the contours as SVG drawings,
2.Render consecutive sliced using py-rsvg library as PIL image and then
express as NumPy array (as in svg_renderer.py::_renderImage)
3.Process all slides this way and put them into common NumPy array.
4.Use python-nifti (niftilib.sourceforge.net/pynifti/) to store the
volume as niftii volume (see vtkgui.py::exportToNiftii for example code).
5.Threshold the volume extracting desired values then apply the marching
cubes algorithm. I cannot suggest you any library beside VTK but I am
sure that you can easily google one.

Note that you will have to implement additional inter-slice
interpolation routine that will handle non-uniform slice spacing.

Alternatively, directly from the contours:
* Braude et al. - Contour-based surface reconstruction using MPU implicit models - 2007.pdf
* Piecewise-Linear Interpolation between Polygonal Slices - Barequet.pdf
* Wang et al. - Efficient surface reconstruction from contours based on two-dimensional Delaunay triangulation - 2006.pdf

"""