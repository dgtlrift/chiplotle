from chiplotle.hpgl.label import Label as HPGLLabel
from chiplotle.hpgl.commands import PA
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.shape import _Shape
from chiplotle.tools import mathtools
from autologging import logged, traced
import math

## TODO should a Label be a path? Probably not.

@traced
@logged
class Label(_Shape):
    '''
    A text label.

    - `text` is the text to be displayed.
    - `charwidth` is the width of characters in cms.
    - `charheight` is the height of characters in cms.
    - `charspace` is the spacing factor between characters.
    - `linespace` is a spacing factor between lines.
    - `origin` is the origin of the text, can be:
            'top-left'     'top-center'      'top-right'
            'middle-left'  'middle-center'   'middle-right'
            'bottom-left'  'bottom-center'   'bottom-right'
    '''

    HPGL_ORIGIN_MAP = {
        'bottom-left'  : 1,
        'middle-left'  : 2,
        'top-left'     : 3,
        'bottom-center': 4,
        'middle-center': 5,
        'top-center'   : 6,
        'bottom-right' : 7,
        'middle-right' : 8,
        'top-right'    : 9}


    def __init__(self,
        text,
        charwidth,
        charheight,
        charspace = None,
        linespace = None,
        origin = 'bottom-left'):

        _Shape.__init__(self)

        self.text = text
        self.charspace = charspace
        self.linespace = linespace
        self.origin = origin
        self.__log.debug( "origin %s" % origin)
        self.points = [(0, 0), (charwidth, 0), (charwidth, charheight)]

        self.never_upside_down = False

    ## PUBLIC PROPERTIES ##

    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, arg):
        self._points = CoordinateArray(arg)


    @property
    def angle(self):
        return self.points.difference[0].angle

    ## TODO make settable...
    @property
    def charwidth(self):
        return self.points.difference[0].magnitude
#   @charwidth.setter
#   def charwidth(self, arg):
#      self._points

    @property
    def charheight(self):
        return self.points.difference[1].magnitude

    ## PRIVATE PROPERTIES ##

    @property
    def _infix_commands(self):
       angle = self.angle
       if self.never_upside_down:
          if math.pi * 3 / 2.0 > angle > math.pi / 2.0:
             angle += math.pi

       if _Shape.language == 'HPGL':
          origin = self.HPGL_ORIGIN_MAP[self.origin]
          self.__log.debug( "origin %s" % origin )
          label = HPGLLabel(
             text = self.text,
             charwidth = self.charwidth,
             charheight = self.charheight,
             charspace = self.charspace,
             linespace = self.linespace,
             origin = origin,
             direction = mathtools.polar_to_xy((1, angle)),
             )
          return [PA(self.points[0]), label]

       elif _Shape.language == 'gcode':
          self.__log.warning( 'Sorry, no g-code support!' )
          raise NotImplementedError


    def cat(self,
        text,
        charwidth,
        charheight,
        charspace = None,
        linespace = None,
        origin = 'bottom-left'):

        self.text += text
        self.charspace = charspace
        self.linespace = linespace
        self.origin = origin
        self.__log.debug( "origin %s" % origin)
        self.points = [(0, 0), (charwidth, 0), (charwidth, charheight)]
        return(self)	

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self.text)

## DEMO CODE

if __name__ == '__main__':
    from chiplotle import *
    from chiplotle.hpgl.formatters import Pen
    from autologging import TRACE
    import logging
    import sys

    logging.basicConfig(level=TRACE, stream=sys.stdout,
       format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")

    pl = instantiate_virtual_plotter()
    pl.margins.soft.draw_outline()

    lbtc = Label("Hello!", 1, 2, origin = 'bottom-center')
    Pen(1)(lbtc) ## we need this for Label to display with hp2xx

    rotate(lbtc, 3.14 / 4 * 3)

    lbbl = Label("Bot-Left!", 1, 2, origin = 'bottom-left')
    Pen(2)(lbbl) ## we need this for Label to display with hp2xx
 
    lbml = Label("Mid-Left!", 1, 2, origin = 'middle-left')
    Pen(3)(lbml) ## we need this for Label to display with hp2xx
 
    lbtl = Label("Top-Left!", 1, 2, origin = 'top-left')
    Pen(4)(lbtl) ## we need this for Label to display with hp2xx
 
    lbbc = Label("Bot-Cent!", 1, 2, origin = 'bottom-center')
    Pen(5)(lbbc) ## we need this for Label to display with hp2xx
 
    lbmc = Label("Mid-Cent!", 1, 2, origin = 'middle-center')
    Pen(6)(lbmc) ## we need this for Label to display with hp2xx
 
    lbbr = Label("Bot-Right!", 1, 2, origin = 'bottom-right')
    Pen(7)(lbbr) ## we need this for Label to display with hp2xx
 
    lbmr = Label("Mid-Right!", 1, 2, origin = 'middle-right')
    Pen(1)(lbmr) ## we need this for Label to display with hp2xx
 
    lbtr = Label("Top-Right!", 1, 2, origin = 'top-right')
    Pen(2)(lbtr) ## we need this for Label to display with hp2xx

    lbcat = Label("Bot-Cent!\n\r", 1, 2, origin = 'bottom-center')
    #Pen(1)(lbtc) ## we need this for Label to display with hp2xx

    lbcat = lbcat.cat("Bot-Left!\n\r", 1, 2, origin = 'bottom-left')
    #Pen(2)(lbbl) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Mid-Left!\n\r", 1, 2, origin = 'middle-left')
    #Pen(3)(lbml) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Top-Left!\n\r", 1, 2, origin = 'top-left')
    #Pen(4)(lbtl) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Bot-Cent!\n\r", 1, 2, origin = 'bottom-center')
    #Pen(5)(lbbc) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Mid-Cent!\n\r", 1, 2, origin = 'middle-center')
    #Pen(6)(lbmc) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Bot-Right!\n\r", 1, 2, origin = 'bottom-right')
    #Pen(7)(lbbr) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Mid-Right!\n\r", 1, 2, origin = 'middle-right')
    #Pen(1)(lbmr) ## we need this for Label to display with hp2xx
 
    lbcat = lbcat.cat("Top-Right!\n\r", 1, 2, origin = 'top-right')
    #Pen(2)(lbtr) ## we need this for Label to display with hp2xx

    rotate(lbcat, 3.14 / 4 * 3)

    c = circle(100 / 2.5)
    g = group([c, lbtc, lbbl, lbml, lbtl, lbbc, lbmc, lbbr, lbmr, lbtr, lbcat])

    center_at(g, [100,100])

    pl.write(g)
    io.view(pl)

