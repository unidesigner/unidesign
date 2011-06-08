""" Polygon Mesh Geometry

See http://en.wikipedia.org/wiki/Polygon_mesh

Book: Polygon Mesh Processing
http://www.crcpress.com/ecommerce_product/product_detail.jsf?isbn=9781568814261

"""


class PolygonMesh(object):
    """ A polygon mesh or unstructured grid is a collection of vertices,
    edges and faces that defines the shape of a polyhedral object.

    The faces usually consist of triangles, quadrilaterals or other simple convex polygons,
    but may also be composed of more general concave polygons, or polygons with holes.
    """
    pass

class FaceVertexMesh(PolygonMesh):
    """ Face-vertex meshes represent an object as a set of faces and a set of vertices.
    """
    def __init__(self, vertices, faces):
        """

        Parameters
        ----------
        vertices : Nx3, ndarray
            Array of vertex positions
        faces : NxM, ndarray
            Array of M-faces
        
        """
        self.vertices = vertices
        self.faces = faces


class WingedEdgeMesh(PolygonMesh):
    pass

class RenderDynamicMesh(PolygonMesh):
    pass

class VertexVertexMesh(PolygonMesh):
    pass