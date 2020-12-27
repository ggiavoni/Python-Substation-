"""Retorna a Quantidade de Equipamentos da Categoria Electrical Equipment \n \n Autor: Paulo Giavoni"""

# Importa o API do Revit
from Autodesk.Revit import DB

# Active Document from Revit
doc = __revit__.ActiveUIDocument.Document

# Create Filtered Element Collector
collector = DB.FilteredElementCollector(doc)

# Create Filter
filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_ElectricalEquipment)

# Apply Filter
electricalEquipment = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

# All Families
all_fams = DB.FilteredElementCollector(doc).OfClass(DB.Family).WhereElementIsNotElementType().ToElements()

family_name = []
type_name = []
# filtra electrical equipment de todas as familias do projeto ativo
for fam in all_fams:
    fam_name = fam.FamilyCategory.Name
    if fam_name == "Electrical Equipment":
        ele_name = fam.Name
        family_name.append(ele_name)

# retorna o nome dos tipos das categorias em apply filter
for electricalEquipments in electricalEquipment:
    Type_Name = electricalEquipments.Name
    if Type_Name:
        type_name.append(Type_Name)

print(family_name)
print(type_name)