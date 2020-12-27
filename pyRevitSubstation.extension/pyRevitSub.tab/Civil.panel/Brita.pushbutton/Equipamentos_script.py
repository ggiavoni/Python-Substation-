"""Calcula a quantidade em metros da categoria FlexPipe \n \n Autor: Paulo Giavoni"""

# Importa o API do Revit
from Autodesk.Revit import DB

# Documento atual do Revit
doc = __revit__.ActiveUIDocument.Document

# Create Filtered Element Collector
collector = DB.FilteredElementCollector(doc)

# Create Filter
filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_FlexPipeCurves)

# Apply Filter
flex_pipe = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

start_len = 0
name = []
length = []

# looping for all the elements
for flex_pipes in flex_pipe:
    len_param = flex_pipes.Parameter[DB.BuiltInParameter.CURVE_ELEM_LENGTH]
    type_name = flex_pipes.Name
    if len_param:
        total_len = start_len + (len_param.AsDouble() * 0.3048)
        length.append(total_len)
    if type_name:
        name.append(type_name)

x = zip(name, length)


def getkey(item):
    return item[0]


lista_final = sorted(x, key=getkey)

output = []
last = None
for type, amount in lista_final:
    if type != last:
        output.append([type, 0])
        last = type
    output[-1][1] += amount

print(('\n'.join(['%i: %s' % (n, output[n]) for n in xrange(len(output))])))

