#made by Taco Pover
import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('System')		
from System.Collections.Generic import List

if isinstance(IN[0][0], list):
	curvepoints = IN[0]
else:
	curvepoints = [IN[0]]

if isinstance(IN[1], list):
	systype = UnwrapElement(IN[1])
else:
	systype = [UnwrapElement(IN[1])]
sl = len(systype)

flextype = UnwrapElement(IN[2])

if isinstance(IN[3], list):
	level = UnwrapElement(IN[3])
else:
	level = [UnwrapElement(IN[3])]
ll = len(level)

if isinstance(IN[4], list):
	diameter = IN[4]
else:
	diameter = [IN[4]]
dl = len(diameter)

metric = doc.DisplayUnitSystem == DisplayUnit.METRIC

def createFlexPipe(systype,levelid,starttan,endtan,points,diameter):
	flex = Plumbing.FlexPipe.Create(doc,systype,flextype.Id,levelid,starttan,endtan,points)
	param = flex.get_Parameter(BuiltInParameter.RBS_PIPE_DIAMETER_PARAM)
	if metric:
		param.Set(diameter/304.8)
	else:
		param.Set(diameter)
	return flex
	
	
def createFlexDuct(systype,levelid,starttan,endtan,points,diameter):
	flex = Mechanical.FlexDuct.Create(doc,systype,flextype.Id,levelid,starttan,endtan,points)
	param = flex.get_Parameter(BuiltInParameter.RBS_CURVE_DIAMETER_PARAM)
	if metric:
		param.Set(diameter/304.8)
	else:
		param.Set(diameter)
	return flex

newflex = []

TransactionManager.Instance.EnsureInTransaction(doc)
for i,p in enumerate(curvepoints):
	levelid = level[i%ll].Id
	sysid = systype[i%sl].Id
	diam = diameter[i%dl]
	
	points = List[XYZ]()
	for x in p:
		points.Add(x.ToXyz())
		
	starttang = points[1].Subtract(points[0])
	last = points.Count - 1
	secondlast = last -1
	endtang = points[last].Subtract(points[secondlast])

	if flextype.GetType() == Plumbing.FlexPipeType:
		flex = createFlexPipe(sysid,levelid,starttang,endtang,points,diam)
	else:
		flex = createFlexDuct(sysid,levelid,starttang,endtang,points,diam)

	newflex.append(flex.ToDSType(False))
	
TransactionManager.Instance.TransactionTaskDone()

			

OUT = newflex
