from chiplotle.core.cfg.cfg import __version__
__authors__ = "Victor Adan, Douglas Repetto"
__license__ = "GPL"
__url__     = "http://music.columbia.edu/cmc/chiplotle"
__doc__     = \
"""Chiplotle
Python library for pen plotting.

Copyright %s
Version %s
License %s
Homepage %s

""" % (__authors__,__version__,__license__,__url__)


## IMPORTS ##

from chiplotle.core import errors

from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.coordinate import Coordinate

from chiplotle.hpgl.commands import *
from chiplotle.hpgl.compound import *
from chiplotle.hpgl.compound.decorators import *
from chiplotle import plotters
from chiplotle.tools import *

from chiplotle.tools.plottertools import instantiate_plotters


## remove unnecessary modules...
#globals().pop('cfg')
globals().pop('hpgl')
#globals().pop('interfaces')
globals().pop('tools')
globals().pop('utils')
