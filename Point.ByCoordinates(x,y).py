# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
import clr
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
start = IN[0]
step = IN[1]
stop = IN[2]
family = IN[3]
level = IN[4]

list = []

# Place your code below this line

for x in range(start, stop, step):
	for y in range( start, stop, step):
		list.append(Revit.Elements.FamilyInstance.ByPointAndLevel(family,Point.ByCoordinates(x,y),level))
		


# Assign your output to the OUT variable.
OUT = list
