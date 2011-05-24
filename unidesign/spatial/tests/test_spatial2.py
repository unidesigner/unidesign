""" Load Region from NeuroHDF and apply measures to retrieved trees """

from unidesign.spatial.group import Region, Treelines, Connectors
from neurohdf import File

f = File('mydataset.nh5', 'r')

# wrap a region

# importance of the ability to select/deselect, group elements