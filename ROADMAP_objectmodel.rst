# Recommendation for NeuroHDF hierarchical layout

# Provide a one-on-one mapping from Groups to Python classes.
# e.g. the Group name represents an instance, and it has a attribute
# "type"/"class" denoting the class name

/root

    /Group:Region (define namespace: neuroscience.spatial.microscale )


        /Dataset:Metadata
            Data: (encoded as JSON byte-string, or XML-encoded specification)

        # or

        /Group:Metadata
            /Dataset:NineML
            /Dataset:JSON
            /Dataset:... (the semantic references?)

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

            /Dataset:Surface0001
                Attributes:
                Data: comprises vertices & surfaces, so must be a group, see below

            /Group:Surface0001
                Attributes:

                /Dataset:vertices
                /Dataset:faces
                
        /Group:3DVolumes

            /Dataset:Volume0001
                Attributes:
                    dimension: (int,int,int)
                    resolution: (int,int,int)
                    ...
                Data: NxMxP array

        /Group:2DContours
            # Can contain closed/open contours (per slice?)
            
            /Dataset:Contour001

            /Dataset:Contour002

        /Group:Forest/TreeRegion/TreeConnectorRegion
        # Question: with a TreeRegion, is this breaking the semantics with a
        # Region that can have trees as their parts?

            # Design decision: either
            # 1. one dataset containing all the trees with label array to select
            # 2. multiple dataset objects containing only one tree
            # Criteria: efficiency to load/store/access ? overhead?

            /Dataset:verticesid
            /Dataset:verticeslocation
            /Dataset:globaltopology
            /Dataset:localtopology
            /Dataset:labeling
            /Dataset:coloring

            # If we want to store Connectors, they must go into the
            # Forest and be indexed in the globaltopology