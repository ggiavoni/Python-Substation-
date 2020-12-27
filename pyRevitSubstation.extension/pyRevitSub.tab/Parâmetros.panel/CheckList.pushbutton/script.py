"""O Nome de Todas as Familias no Projeto\n \n Autor: Paulo Giavoni"""

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
cat_name = []
# filtra a categoria de todas as familias do projeto ativo
for fam in all_fams:
    fam_name = fam.FamilyCategory.Name  # Nome da Categoria
    ele_name = fam.Name  # Nome do Elemento que Pertence a Categoria
    if fam_name == "Electrical Equipment":
        family_name.append(ele_name)
    if fam_name == "Data Devices":
        cat_name.append(ele_name)


print("----------------------CATEGORIA EQUIPAMENTOS ELETRICOS-------------------------")
for a in family_name:
    print('\"{}\"'.format(a))

print("----------------------CATEGORIA CONECTORES E AFINS-----------------------------")
for a in cat_name:
    print('\"{}\"'.format(a))