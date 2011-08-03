euroHDF
========
NeuroHDF defines a hierarchical layout to represent multi-scale, multi-modal neuroscientific datasets based on HDF5.

NeuroHDF enables storage and fast access of large datasets. It can be used to store time series data (behavior,
 measured and simulated physiology, simulation data, point processes) and structural data (anatomy, static and
 dynamic networks).

Basic idea: Use generalized N-dimensional homogeneous array together with metadata structured in a hierarchical manner.

Implement a first draft of a "NeuroHDF" layout according to the principles outlined in `Unifying Biological Image Formats with HDF5 <http://queue.acm.org/detail.cfm?id=1628215>`_

There is the BioHDF initiative, with very similar goals. Their specification is here:
* http://www.hdfgroup.org/projects/biohdf/biohdf_documentation.html
* http://finchtalk.geospiza.com/2010/04/bloginar-standardizing-bioinformatics.html

HDF5 forum
* http://hdf-forum.184993.n3.nabble.com/

Hierarchical Design
-------------------

Data types
**********

NAME
Synonyms:
Application examples:
Mappable existing binary file formats:
Reusable existing XML markup languages:

Required attributes
Recommended attributes:
Optional attributes:

Dataset types (axes type, and content type):
- non-spatiotemporal entity
- spatial entity
- temporal entity
- spatiotemporal entity
- generalized spatiotemporal entity

xspace, yspace, zspace, time
xfrequency, yfrequency, zfrequency, tfrequency

Define a mapping between INDEX space and "WORLD" space

offset would shift the AXES.

Dictionary metadata:
- bb

* If grouping on the same hierarchical level, one axes has to serve as an "alignment" axes, representing e.g. subjects.
  Usually these are the rows.

Advantages / Disadvantages for separating/not-separating out big blobs
--------------------------
* Extended metadata description required for a subset
* Requirements of fully filled array not enforcable (e.g. missing conditions for a subject)
* Enforcement of a global data type would be enforced for the whole blob
* Dimensions with only one element might be used to break up

Design Goals
------------
* Propose the hierarchical layout with groups and datasets, only later define a set of core characteristics for a valid standard
* Specify group layout convention
* Specify usage of attributes
* Unicode support?
* Self-documenting I/O format

Compatability/Export
--------------------
* NeuroML: http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1000815
* NineML: http://www.nineml.org/news/news.shtml
* Learn from Bioinf community: http://abhishek-tiwari.com/2009/02/comparison-of-cellml-and-sbml.html

Interfacing with Simulation Environments
----------------------------------------
Based on the review "Computer Simulation Environments" by Gleeson et al.

* NEURON
  * section object for cable modelling? section = (line) segment?
  * Import/Export in NeuroML format
* GENESIS
  * OO elements that communicate with each other (about 130 objects)
* NEST
  * See connectivity specification

Resources
---------
* ModelDB web site: http://senselab.med.yale.edu/modeldb
* NeuronDB web site: http://senselab.med.yale.edu/neurondb
* http://www.NeuroMorpho.Org
* http://mattions.github.com/neuronvisio/index.html
* SWC Databases http://krasnow.gmu.edu/cn3/L-Neuron/database/index.html

Datastructures
--------------
Tree
http://en.wikipedia.org/wiki/Tree_%28data_structure%29
http://en.wikipedia.org/wiki/Binary_heap

Need to represent:
1) spiking neurons -> NineML?
2) synapses -> connectors
3) populations of neurons and -> region with trees and connectors
4) connectivity patterns across populations of neurons, or classes of neurons

Hierarchical Layout Recommendation
----------------------------------

Idea:
Integrate groups into one single nd-array by defining per axes:
* name, e.g. x,y,z,t,channel,parameter[x=3]
* unit, e.g. m, m**2, m**-0.5, m*s**-1, or m2 or m/s, or 1 for generic axes
* semantic interpretation, right (towards right is positive x axes)
3D spatial axes define a right hand coordinate system.

seperate affine transformation in 3d rotation, and a seperate vector for the offset.

Binary blob object:
* Attributes: name, unit, worldspace semantics
* affine (rotational component), offset
* FOR a (spatial) REGION


- **Root**
  *The top-level node of the hierarchy. Project/subject nodes might be injected higher.*

  - Global attributes
    creator: The creator of the dataset including email
    collaborators: The collaborators related to the creation of the dataset
    references: Citation or URL reference for this dataset
    title: A generic title
    species: The biological organism this dataset is representing
    description: A generic prose description of the content and purpose of the dataset
    created: Creation timestamp
    modified: Modification timestamp

  - **Group:Physiology**: *High-level node for physiological datasets, possibly associated with anatomy*
  - **Group:Simulation**: *High-level node for data produced by (neuronal) simulators*
  - **Group:Behavior**: *Behavioral measurements*
=======
- **Root**

  - **Group:Network**

  *Other names: Connectionmatrix/Graph/Circuitry/ConnectivityDiagram.
  It can contain a (sparse) connectivity matrices, with row labeling, maybe also representing hierarchical networks*

  - **Group:Region**

  *Defines the spatial container region for datasets of different types in the subhierarchy
  dataset can contain multiple Regions*

      - Attributes

        id : int
            Need Region id as hash id and for RegionConnector specification
        dimension: (int,int,int)
            The spatial extent on three axes x,y,z
        resolution: (float,float,float)
            The spatial resolution on three axes x,y,z
        unit: (str,str,str)
            The unit abbreviation on the three axes x,y,z
        affine: (4,4) array
            Transforms container region from root-space (one level higher space) to Region-space
            # What would affines for individual Groups mean?

        namespace
            e.g. neuroscience.anatomy.microscale

      - **Group:Metadata**
        *Metadata organised as XML file, byte-encoded as 1D byte array*
        - Dataset:NineML
        - Dataset:JSON
        - ...

      - **Group:2DSliceSet**

      *A set of 2D slices. If aligned, it represents an ImageStack. Useful when it is required
      to store affines for each slice seperately. Also consider volume group to represent the data*

        - Attributes

          name
              A name/title for the set of slices

          description
              A description for the set of slices

          number_of_slices
              The number of slices

          slicename_pattern
              Regex pattern for slice names

        - Dataset:Slice0001

            - Attributes

              dimension: (int,int)

              resolution: (int,int)

              resolution unit
                  str, e.g. 'nm'

              zindex : int

              affine: (4,4) array

            - Data : NxM array

        - Dataset:Slice0002

        - Dataset:Slice0003

      - **<Group>SurfaceMesh**
      attr:
      - type: FaceMesh
      dataset
      - vertices

        spatiotemporal entity
        x,y,z,t
        at least one spatial, only spatial axes is implicitly interpreted as on time point

        generalized spatiotemporal entity
        x,y,z,t,channel1,channel2,channel3,subject
        

      - topology

        topotemporal entity


      - **Group:PolygonMeshSet**

      *Would store polygonal-based surface meshes*

          - Group:Surface0001

              - Attributes:

                name
                    surfaces0001, but already in group name.

                type
                    e.g. FaceMesh

              - Dataset:vertices

              - Dataset:faces

      *Or if piling all together*
      Group:Points/Connectivity

      - **Group:3DVolumeSet**

        - Dataset:Volume0001

            - Attributes

              dimension: (int,int,int)

              resolution: (int,int,int)

              resolution_unit: (.., .., ..)

              ...

            - Data: NxMxP array

      - **Group:2DContourSet**

      *Can contain closed/open contours (per slice?)*

        - Attributes:-

        - Dataset:Contour001

            - Attributes

              type: open

            - Data
            
              [0.0, 10.3]
              [5.3, 53.2]
              ....

        - Dataset:Contour002

      - **Group:TreeSet**

      *Other names are Treelines/Skeletons/Trees/Arbors. Analogous to stacked SWC files*

        - **Group:Points**

            - Dataset:data

                - Attributes

                  format: 'xyz'

                - Data

                  [12.3, 34.2, 10.3]
                  [42.3, 14.2, 14.3]
                  ...

            - Group:Concept

            *For better performance, store [id, startidx, endidx] for indexing into points
            instead doing integer selections on the id*

                - Attributes

                  name
                      id

                  description
                      'Point identifiers derived from the database'

            - Group:Concept

                - Attributes

                  name
                      labels

                  description
                      'Semantics of the points'

                  mapping
                      '{u"1": u"axon", u"2" : u"soma", u"3" : u"dendrite"}'

                - Dataset:data
                
                        1
                        1
                        2
                        3
                        3
                        .
                        .

            - Group:Concept

                - Attributes

                  name
                      'colors'

                  description
                      'A Nx4 array storing unsigned byte color values'

                  format
                      'RGBA', should be according to graphics specs

                - Dataset:data
                
                    [10,20,30,255]
                    [10,20,30,255]
                    ...

            *More concepts: radius, confidence, cell class, scalar / vector / tensor*

        - **Group:Connectivity**

        *Rather store full connectivity [fromidx, toidx] rather than parent-child
        with -1. advantage of using unsigned int. similarly for triangles [firstidx,secidx,thirdidx]*

            - Dataset:data

                *Adds the offset to the ordered trees to make indexing global into the Points*

                - Attributes

                    topology: global

                - Data

                    [0,-1]
                    [1, 0]
                    [2, 0]
                    [3, 1]
                    ...

            - Dataset:data

                *Adds the offset to the ordered trees to make indexing global into the Points*

                - Attributes

                    topology: global

                - Data

                    [0,-1]
                    [1, 0]
                    [2, 0]
                    [3, 1]
                    ...

            - Group:Concept

                - Attributes

                  name: localtopology

                  description: 'Connectivity per tree, thus defined locally and in accordance with Points ordering'

                - Dataset:data

                        [0,-1]
                        [1, 0]
                        [2, 0]
                        [3, 1]
                        [4, 2]
                        [0,-1]
                        [1, 0]
                        ...

                - Group:Trees

                    *here you could store tree-based tags, e.g. associated with the tree id*

                    - Group:Concept

                        - Attributes:

                            type : aabb
                                Store axis aligned bounding boxes for each tree

                        - Dataset:data

                            [id, lower, upper]
                            [123, x0, y0, z0, x1, y1, z1]
                            ....

        - **Group:Connectors**

        *Connectors are M:N relations between treeline nodes
        they have a spatial location themselves, and are associated
        with the Treelines Group, using global indexing*

            - Attributes

            - Group:Points

                *comment: a pure topological connection without spatial
                location could use -1 as replacement coordinates*

                - Dataset:data

                    - Attributes

                        format: 'xyz'

                        [2.3, 74.2, 14.3]
                        [62.3, 24.2, 64.3]
                        ...

                - Group:Concept

                    *e.g associated IDs, types*

            - Group:Connectivity

                *expresses the connectivity of treenodes to connector index
                this information is directional*

                - Dataset:data_pre_conn

                - Dataset:data_post_conn

        - **Group:PointCloud**

        *e.g. vertices without connectivity but radius and color attributes*

Open Issues
===========

* Should the layout recommendation propose `level of detail representations <http://books.google.com/books?id=CB1N1aaoMloC&pg=PA9&lpg=PA9&dq=represent+levels+of+details&source=bl&ots=eaHOdD0-1j&sig=3Gp_ub9UAr94aBFHN3lzKkW_QNM&hl=en&ei=02f9Taa3Lsj50gHHq4iWAw&sa=X&oi=book_result&ct=result&resnum=8&ved=0CEIQ6AEwBw>`_?
* How to deal with missing slices?
* Is SliceSet efficient for thousands of slices?
* How to store connectors? Is post_conn directionality OK? alternatively or have another column defining the type/directionality?
  What do you possibly want to store?
* Provide a one-on-one mapping from Groups to Python classes, e.g. the Group name represents an instance, and it has a attribute "type"/"class" denoting the class name
* Check if nothing is missing from what is expressible in `FieldML/MeshML <http://www.physiome.org.nz/xml_languages/fieldml/documents/meshml_fieldml.html/>`_

Examples
========

Neuroimaging
------------

- Group:Region

  - Attributes

        namespace: neuroscience.anatomy.macroscale

        dimension:

        resolution: (1.0, 1.0, 1.0)

        resolution_unit: ('mm', 'mm', 'mm')

        affine: np.eye(4)

  - Group:3DVolumeSet

        *a three-dimensional volumetric dataset converted from Nifti-1*

  - Group:PolygonMeshSet

        *a three-dimensional surface dataset converted from Gifti*

  - Group:FiberSet

        *A three-dimensional fiber tractography dataset converted from TrackVis*
        
