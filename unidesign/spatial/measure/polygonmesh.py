""" Measures for polygon meshes """

__copyright__ = "Copyright 2011, UniDesign Development Team"
__license__ = "BSD"
__authors__ = ["Stephan Gerhard <connectome@unidesign.ch>"]

import numpy as np

from ..geometry import polygonmesh

def surface_area(polygon_mesh):
    """ Computes the surface area for a polygon mesh.

    Parameters
    ----------
    polygon_mesh : ``PolygonMesh`` object

    Returns
    -------
    result : surface area

    """
    if isinstance(polygon_mesh, polygonmesh.FaceVertexMesh):
        print("A FaceVertex Mesh")
        result = 0.0
        for face in polygon_mesh.faces:
            v1, v2, v3 = face
            result += 0.5 * abs(np.linalg.norm(
                np.cross(
                    polygon_mesh.vertices[v2]-polygon_mesh.vertices[v1],
                    polygon_mesh.vertices[v3]-polygon_mesh.vertices[v1] )))
        return result

    return None