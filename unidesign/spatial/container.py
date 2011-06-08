
# TODO: add Group and/or Selection

class Region(object):
    """ Base class for a spatial Region container

    A Region can contain simple and advanced geometry.

    A Region can be thought of as a 3D analogy to a sheet of
    paper in 2D. A Region defines its own coordinate system,
    dimension and resolution.

    """

    def __init__(self, **attr):
        """ Initialize a region

        Parameters
        ----------
        dimension ; array-like, integer
            The number of units in each spatial direction
            e.g. [1000,2000,400]

        resolution : array-like, double
            The resolution in each spatial direction
            e.g. [2.5, 3.0, 10.23]

        resolution_unit : array-like
            The unit of resolution in each spatial direction
            e.g. ['nm', 'nm', 'nm']

        origo : array-like
            The locus of the origo of the coordinate system
            XXX: in relation to some global coordinate system (?)
                 this could be implied in the affine

        axes_orientation : array-like
            The orthogonal orientation of the x-, y- and z-axes
            of a cartesian coordinate system as a 3x3 array.

        coordinate_system : ['left-handed', 'right-handed']
            (default='left-handed')

        affine : array-like
            origo and axes_orientation can be grouped in a 4x4 affine
            array. TODO: correct?

        extension : ['bounded', 'unbounded']
            Defining a dimension implies a bounded Region

        name : string, optional (default='')
            An optional name for the Region.

        attr : keyword arguments, optional (default=no attributes)
            Attributes to add to a graph as key-value pairs.
        """
        pass

    def __str__(self):
        """Return the Region name.

        Returns
        -------
        name : string
            The name of the Region.
        """
        return self.name