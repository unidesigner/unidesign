""" Treenodes / Connectors """

"""
* Geometry (spatial location, location) is well-separated from any semantic annotation
* Topology is stored in an efficient way for analysis and visualization
* Both treenodes and connectors are part of a project which defines underlying space
* Metadata annotation is achieved using attributes on nodes
"""

/treenodes
    
    /spatial_location
    
        /data
            [x, y, z]
            [1, 3, 1]
            [5, 2, 2]
            [7, 4, 2]
            [1, 3, 1]
            [5, 2, 2]
            [7, 4, 2]
                
        /conceptX (tree_id, labeling, radius, confidence, color, scalar / vector / tensor)
        
        /concept {'name' :  'XXX', 'type' : 'conceptual/quantitative/...', 'range' : '...',
                  'value' : { 1 : 'axon', 2 : 'dendrite', 3 : 'cellbody' } }
            /data
            [1, 3, 2, 1, 1, 3]
    
        e.g.
        /concept {'name' : 'treeid', 'value' : { 1 : 'mytree1', 2 : 'mytree2' } }
            /data
            [1, 1, 1, 2, 2, 2]
         
        /associated_data
            meshes, volumes, timeseries, ....
    
    /topology
    
        /local_topology # indices to the treenodes. the indices are implicitly defined through spatial_location order
        [-1, 0, 0, 1, 1, 2, -1, 0, 1, 1, 2]
        [ 0, 1, 2, 3, 4, 5,  0, 1, 2, 3, 4]
    
        /global_topology
        [-1, 0, 0, 1, 1, 2, -1, 6, 7, 7, 8]
        [ 0, 1, 2, 3, 4, 5,  6, 7, 8, 9,10]        
        
        /conceptX (labeling, radius, confidence, color, scalar / vector / tensor)
    

/connectors

    /spatial_location
    
        /data
            [x, y, z]
            comment: a pure topological connection without spatial
            location could use -1 as replacement coordinatse
            
        /conceptX

        /associated_data
            meshes, volumes, timeseries, ....
    
    /topology
    
        /global_topology
            [preid, postid]

        /conceptX
