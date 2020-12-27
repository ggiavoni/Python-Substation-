# Python para Subestações de Energia com BIM 
> Criação de Extensões em Python na plataforma PyRevit que utliza o PythonShell.

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

Objetivo: Quantitativos específicos para o Revit, onde o usuário irá apenas clicar em um botão e extrair o quantitativo de uma categoria específica. A ideia principal é reduzir o tempo de tal função para novos usuários, ou principalmente, aqueles que apenas desejam consultar informação. 

![](../header.png)

## Instalação das Ferramentas Python-Substation

## Passo 01: Instale o PyRevit
Plataforma criada por Ehsan Iran-Nejad que serve como ponte entre C# e Python: 

[PyRevit - Página de Instalação](https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d)

## Passo 02 

Procure este caminho após a instalação: 

C:\Users\USER\AppData\Roaming\pyRevit-Master\extensions

Para que uma nova aba, personalizada, apareça no Revit junto aos já existentes do PyRevit, você precisa que as pastas e subpastas estejam organizadas da seguinte forma:                                             
* 1.0.1
    * Baixe e cole dentro de extensions [pyRevitSubstation.extension](https://github.com/ggiavoni/PythonSubstation-/tree/main/pyRevitSubstation.extension/pyRevitSub.tab)
* 1.0.2
    * Clique em PyRevit e aplique o Reload para que a pasta apareça no Revit. 
 
## Exemplo de uso

Alguns exemplos interessantes e úteis sobre como seu projeto pode ser utilizado. Adicione blocos de códigos e, se necessário, screenshots.

_Para mais exemplos, consulte a [Wiki][wiki]._ 

## Configuração para Desenvolvimento

Descreva como instalar todas as dependências para desenvolvimento e como rodar um test-suite automatizado de algum tipo. Se necessário, faça isso para múltiplas plataformas.

```sh
make install
npm test
```

## Histórico de lançamentos

* 0.2.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 0.2.0
    * MUDANÇA: Remove `setDefaultXYZ()`
    * ADD: Adiciona `init()`
* 0.1.1
    * CONSERTADO: Crash quando chama `baz()` (Obrigado @NomeDoContribuidorGeneroso!)
* 0.1.0
    * O primeiro lançamento adequado
    * MUDANÇA: Renomeia `foo()` para `bar()`
* 0.0.1
    * Trabalho em andamento

## Meta

Seu Nome – [@SeuNome](https://twitter.com/...) – SeuEmail@exemplo.com

Distribuído sob a licença XYZ. Veja `LICENSE` para mais informações.

[https://github.com/yourname/github-link](https://github.com/othonalberto/)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/yourname/yourproject/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/seunome/seuprojeto/wiki

