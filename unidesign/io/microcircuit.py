""" An API for microcircuit data from CATMAID and NeuroHDF
"""

class Microcircuit(object):

    def __init__(self):
        """
        A  microcircuit consisting of the following data types:
        skeleton, connector
        """
        pass

        # data source:
        # 1. either query CATMAID data model on deman
        # 2. wrap a NeuroHDF dataset

        # want to give it to actor

    def get_vertices(self):
        pass

    def get_connectivity(self):
        pass