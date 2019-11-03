#!/usr/bin/env python
import os
import sys
import re
import fnmatch
from sys import argv
from pprint import pprint


def applyFormula( gcodePath ):

    if os.path.exists( gcodePath ):

        f = open( gcodePath ,"r")
        copy = open( '_' + gcodePath ,"wt")


        current = {'x': 0, 'y': 0, 'z': 0}

        for l in f:

            #Get all current position Values
            cx = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if cx:
                current['x'] = float(cx.group(2))

            cy = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if cy:
                current['y'] = float(cy.group(2))

            cz = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if cz:
                current['z'] = float(cz.group(2))


            # apply formula to current values if are presents in line
            my = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if my:
                l = my.group(1) +   str( formulaY(current)   ) +  my.group(3)


            mx = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if mx:
                l = mx.group(1) +   str( formulaX(current)   ) +  mx.group(3)


            mz = re.match('(.*Y)(\-?[0-9]+\.?\d{0,9})(.*)', l)
            if mz:
                l = mz.group(1) +   str(  formulaZ(current)  ) +  mz.group(3)

            copy.write(str(l)+'\n')

        f.close()
        copy.close()
    else:
        print "ERROR: o gcode file found - " +gcodePath




def formulaX( c ):
    return round(c['x'],2)

def formulaY( c ):
    return round(c['y'],2)

def formulaZ( c ):
    return round(c['z'],2)




if len(sys.argv) > 1:
    applyFormula( sys.argv[1] )
else:
    listOfFiles = os.listdir('.')
    pattern = "*.gcode"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            applyFormula( entry )
    print "gcodes generated with _ prefix"

