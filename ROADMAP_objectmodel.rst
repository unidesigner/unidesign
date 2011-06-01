# Recommendation for the NeuroHDF hierarchical layout

# Provide a one-on-one mapping from Groups to Python classes.
# e.g. the Group name represents an instance, and it has a attribute
# "type"/"class" denoting the class name

# Level of Details in Design?

/root
    Attributes:
        creator:
        collaborators:
        references:

        title:
        species:
        description:

        created:
        ...

    /Group:Physiology
        # Contains physiological datasets, possibly associated with anatomy

    /Group:Simulation
        # Data produced from (neuronal) simulators

    /Group:Behavior
        # Behavioral measurements

    /Group:Connectionmatrix/Graph/Circuitry/ConnectivityDiagram
        # Contains (sparse) connectivity matrices
        # With row labeling
        # also hierarchical!

    /Group:Region
        # defines the container region for datasets of different
        # types in the subhierarchy, dataset can contain multiple Regions

        Attributes:
            id : int
                # needs ids to be used as hash id and for RegionConnector specification
            dimension: (int,int,int)
            resolution: (float,float,float)
            resolution_unit: (str,str,str)
            affine: (4,4) array
                # transforms container region from root-space to Region-space
                # What would affines for individual Groups mean?

            namespace: neuroscience.anatomy.microscale

        /Group:Metadata
            /Dataset:NineML
            /Dataset:JSON
            /Dataset:... (the semantic references?, or XML-encoded specification)

        /Group:2DSlices

            /Dataset:Metadata
                name
                number_of_slices
                slicename_pattern
                ...
                Data: N string array

            /Dataset:Slice0001
                Attributes:
                    dimension: (int,int)
                    resolution: (int,int)
                    resolution unit: str, e.g. 'nm'
                    zindex : int
                    affine: (4,4) array
                Data: NxM array

            /Dataset:Slice0002

            /Dataset:Slice0003

            # can be thousands, yo you want to store them in single datasets?
            # what about "missing" slices

        /Group:3DSurfaces

            /Group:Surface
                Attributes:
                    name: surfaces0001

                /Dataset:vertices

                /Dataset:faces
                
        /Group:3DVolumes

            /Dataset:Volume0001
                Attributes:
                    dimension: (int,int,int)
                    resolution: (int,int,int)
                    resolution_unit: (.., .., ..)
                    ...
                Data: NxMxP array

        /Group:2DContours
            # Can contain closed/open contours (per slice?)
            Attributes:

            /Dataset:Contour001
                Attributes:
                    type: open
                [0.0, 10.3]
                [5.3, 53.2]
                ....

            /Dataset:Contour002

        /Group:Treelines
        # analogous to stacked SWC files

            /Group:Points
                /Dataset:data
                    Attributes:
                        format: 'xyz'

                    [12.3, 34.2, 10.3]
                    [42.3, 14.2, 14.3]
                    ...

                /Group:Concept
                    # for better performance, store [id, startidx, endidx] for indexing into points
                    # instead doing integer selections on the id
                    Attributes:
                        name:id
                        description: 'Point identifiers derived from the database'

                /Group:Concept
                    Attributes:
                        name:labels
                        description: 'Semantics of the points'
                        mapping: '{u"1": u"axon", u"2" : u"soma", u"3" : u"dendrite"}'
                    /Dataset:data
                        1
                        1
                        2
                        3
                        3
                        .
                        .

                /Group:Concept
                    Attributes:
                        name: 'colors'
                        description: 'A Nx4 array storing unsigned byte color values'
                        format: 'RGBA'
                    /Dataset:data
                        [10,20,30,255]
                        [10,20,30,255]
                        ...

                More concepts: radius, confidence, cell class, scalar / vector / tensor

            /Group:Connectivity
                # rather store full connectivity [fromidx, toidx] rather than parent-child
                # with -1. advantage of using unsigned int. similarly for triangles [firstidx,secidx,thirdidx]
                
                /Dataset:data
                    # adds the offset to the ordered trees to make indexing global into the Points
                    Attributes:
                        topology: global
                    [0,-1]
                    [1, 0]
                    [2, 0]
                    [3, 1]
                    ...

                /Group:Concept
                    Attributes:
                        name: localtopology
                        description: 'Connectivity per tree, thus defined locally and in accordance with Points ordering'
                    /Dataset:data
                        [0,-1]
                        [1, 0]
                        [2, 0]
                        [3, 1]
                        [4, 2]
                        [0,-1]
                        [1, 0]
                        ...

            /Group:Trees
                # here you could store tree-based tags, e.g. associated with the tree id

                /Group:Concept
                    Attributes:
                        type : aabb
                    # store axis aligned bounding boxes for each tree
                    /Dataset:data
                        [id, lower, upper]
                        [123, x0, y0, z0, x1, y1, z1]
                        ....

        /Group:Connectors
            # connectors are M:N relations between treeline nodes
            # they have a spatial location themselves, and are associated
            # with the Treelines Group, using global indexing
            Attributes:

            /Group:Points
                # comment: a pure topological connection without spatial
                # location could use -1 as replacement coordinates
                
                /Dataset:data
                    Attributes:
                        format: 'xyz'

                    [2.3, 74.2, 14.3]
                    [62.3, 24.2, 64.3]
                    ...

                /Group:Concept
                    # e.g associated IDs, types

            /Group:Connectivity
                # expresses the connectivity of treenodes to connector index
                # this information is directional
                /Dataset:data_pre_conn

                /Dataset:data_post_conn

                # Question: is post_conn directionality OK? alternatively
                # have another column defining the type/directionality
                # What do you possibly want to store?

        /Group:PointCloud
            # e.g. vertices without connectivity but radius and color attributes