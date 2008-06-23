from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.commands import PU, PD, PA

class Line(_ExtendedHPGL):
   '''Line at absolute position.'''
   def __init__(self, x1, y1, x2, y2):
      _ExtendedHPGL.__init__(self, (x1, y1, x2, y2))
      
   @property
   def _subcommands(self):
      result =[PU( ), 
               PA(self.xy[0:2]),
               PD(self.xy[2:4]),
               PU()]
      return result

