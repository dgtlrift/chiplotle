#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
from chiplotle import *
from chiplotle.hpgl.commands import LB
from autologging import TRACE, logged, traced
import logging
import sys

## HELPER FUNCTIONS ##

def _query_font_size( ):
    char_height = float(raw_input("font height (in cm)? "))
    char_width = float(raw_input("font width (in cm)? "))
    return char_width, char_height

def _query_pen( ):
    pen_num = raw_input("which pen? ")
    if not pen_num:
       pen_num = 1
    pen_num = int(pen_num)
    return pen_num


## MAIN FUNCTION ##

@traced
@logged
def typewriter( ):
    logging.basicConfig(level=TRACE, stream=sys.stdout,
     format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")
    print("***************************")
    print("* CHIPLOTLE TYPEWRITER!!! *")
    print("***************************")
    print("")

#    plotter = instantiate_plotters( )[0]
    plotter = instantiate_virtual_plotter( )

    pen_num = _query_pen( )

    set_size = raw_input("set font size (y/N)? ")

    cw = ch = 1
    if set_size.lower( ) == "y":
        cw, ch = _query_font_size( )
        plotter.write(SI(cw, ch))

    plotter.select_pen(pen_num)

    print("")
    print("type at the >>> prompt.")
    print("press RETURN after each line to be plotted.")
    print("enter a blank line for options.")
    print("")

    finished = False

    growingLabel = None

    while finished == False:
        line = raw_input(">>> ")
        if len(line) == 0:
            print("(enter): blank line")
            print("p: select new pen")
            print("s: set new font size")
            print("q: quit")
            response = raw_input("command: ")
            if response == "p":
                pen_num = _query_pen( )
                plotter.select_pen(pen_num)
            elif response == "s":
                cw, ch = _query_font_size( )
                plotter.write(SI(cw, ch))
            elif response == "q":
                finished = True
            else:
                growingLabel = labelCat(growingLabel, "\n\r", cw, ch)
        else:
            growingLabel = labelCat(growingLabel, line + "\n\r", cw, ch)

    plotter.write(growingLabel)
    io.view(plotter)
    print("l8r.")


if __name__ == '__main__':
    typewriter( )
