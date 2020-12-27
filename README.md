# Python para Subestações de Energia com BIM 
> Criação de Extensões em Python na plataforma PyRevit que utliza o PythonShell.

Objetivo: Quantitativos específicos para o Revit, onde o usuário irá apenas clicar em um botão e extrair o quantitativo de uma categoria específica. A ideia principal é reduzir o tempo de tal função para novos usuários, ou principalmente, aqueles que apenas desejam consultar informação. 

Muitas outras funcionalidades virão por ai, mas para comerçarmos, vamos extrair quantidades!! 

![](../header.png)

## Exemplo de Funcionamento do Código Python com o Revit. 

Instale o [PythonShell](https://github.com/architecture-building-systems/revitpythonshell). 

Vamos criar um script que retorna o nome de todas as famílias do projeto. 

```
# Importa o namespace do Revit 
from Autodesk.Revit import DB

# Documento Ativo do Revit 
doc = __revit__.ActiveUIDocument.Document

# Todas as Famílias do Projeto
all_fams = DB.FilteredElementCollector(doc).OfClass(DB.Family).WhereElementIsNotElementType().ToElements()

family_name = []

# Lógica principal
for fam in all_fams:
    fam_name = fam.FamilyCategory.Name  
    ele_name = fam.Name
    family_name.append(ele_name)
	

print("----------------------NOME DAS FAMILIAS-------------------------")
for a in family_name:
    print('\"{}\"'.format(a))
    

```

## Instalação das Ferramentas Python-Substation

## Passo 1.0: Instale o PyRevit

![](https://github.com/ggiavoni/Python-Substation-/blob/main/1.1.PNG)

Plataforma criada por Ehsan Iran-Nejad que serve como ponte entre C# e Python: 

[PyRevit - Página de Instalação](https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)

## Passo 2.0: Adicione a extensão 

![](https://github.com/ggiavoni/Python-Substation-/blob/main/1.0.PNG)

Procure este caminho após a instalação: 

C:\Users\SeuUsuário\AppData\Roaming\pyRevit-Master\extensions

Cole a pasta disponível em [pyRevitSubstation.extension](https://github.com/ggiavoni/PythonSubstation-/tree/main/pyRevitSubstation.extension/pyRevitSub.tab) neste local. 

Agora abra o Revit, procure a extensão PyRevit e clique em Reload. 
 
## Ferramentas Disponíveis 

**Painel Civil** 

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.2.PNG)

* Função: Retorna a quantidade em m² de alfalto. (Categoria Floor)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.3.PNG)

* Função: Retorna a quantidade em m² de brita. (Categoria Floor)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.4.PNG)

* Função: Retorna o metro linear de canaletas enterradas e suas tampas. (Categoria Wall e Structural Connection)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.5.PNG)

* Função: Retorna a quantidade em m² de alfalto. (Categoria Floor)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.6.PNG)

* Função: Retorna a quantidade em m de cerca de ferramento e o concreto para fixação. (Categoria Site e Floor)
* Status: Em progresso


![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.7.PNG)

* Função: Retorna a quantidade em kg das estruturas metálicas. (Categoria Generic Model)
* Status: Em progresso


![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.8.PNG)

* Função: Retorna a quantidade em Kg e Unidades de Pré-Moldado. (Categoria Generic Model)
* Status: Em progresso

**Painel Eletromecânico**

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.9.PNG)

* Função: Retorna a quantidade de cabos aéreos. (Categoria FlexPipe)
* Status: Finalizado


![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.10.PNG)

* Função: Retorna a quantidade de ferragem para cadeia de isoladores e seus isoladores. (Categoria DataDevices)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.11.PNG)

* Função: Retorna a quantidade de conectores. (Categoria DataDevices)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.12.PNG)

* Função: Retorna a quantidade de eletrodutos, em metros. (Categoria Counduit)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.13.PNG)

* Função: Retorna a quantidade de equipamentos por tensão. (Categoria Electrical Equipment)
* Status: Em progresso

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.14.PNG)

* Função: Retorna a quantidade em metros dos elementos de malha de terra. (Categoria FlexPipe)
* Status: Em progresso

**Painel Parâmetros**

![](https://github.com/ggiavoni/Python-Substation-/blob/main/Imagens/1.15.PNG)

* Função: Retorna o nome de todas as famílias do projeto, conforme filtro pré-estabelecido. 
* Status: Finalizado



