

import numpy as np

from unidesign.spatial.geometry.polygonmesh import FaceVertexMesh
from unidesign.spatial.measure.polygonmesh import surface_area

def test_surface_area():
    a=np.array([[0,0,0],[1,0,0],[0,1,0]], dtype=float )
    b=np.array([[0,1,2]], dtype = int)
    fv = FaceVertexMesh( vertices = a, faces = b )
    area = surface_area( polygon_mesh = fv )
    assert( area == 0.5 )
    