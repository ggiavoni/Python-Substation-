"""Shows the quantities in meters of the category FlexPipe \n \n By: Paulo Giavoni"""

# Import Namespace from Revit
from Autodesk.Revit import DB

# Actual Document or opened project
doc = __revit__.ActiveUIDocument.Document

# Create Filtered Element Collector
collector = DB.FilteredElementCollector(doc)

# Create Filter
filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_FlexPipeCurves)

# Apply Filter
flex_pipe = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

name = []
length = []
output = []

# looping for all the elements
for flex_pipes in flex_pipe:
    len_param = flex_pipes.Parameter[DB.BuiltInParameter.CURVE_ELEM_LENGTH]
    type_name = flex_pipes.Name
    if len_param:
        total_len = 0.0 + (len_param.AsDouble() * 0.30)
        length.append(total_len)
    if type_name:
        name.append(type_name)

# zipping name and length
x = zip(name, length)


# sorting the list
def getkey(item):
    return item[0]


# list sorted
final_list = sorted(x, key=getkey)

# grouping the data in an one single list.
last = None
for type, amount in final_list:
    if type != last:
        output.append([type, 0])
        last = type
    output[-1][1] += amount

# results in PT-BR
for a, b in output:  # <-- this unpacks the tuple like a, b = (0, 1)
    print('ELEMENTO:\"{}\" - COMPRIMENTO:\"{} m"'.format(a, b))

