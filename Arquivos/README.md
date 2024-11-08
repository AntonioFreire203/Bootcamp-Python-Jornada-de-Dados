#Arquivos

## ABRIR ARQUIVO

### Função open()
Para abrir um arquivo, o Python possui a função open().
recebe dois parâmetros: o primeiro é o nome do arquivo a ser aberto, e o segundo parâmetro é o modo que queremos trabalhar com esse arquivo - se queremos ler ou escrever

* através de uma string: "w" (abreviação para
write) para escrita e 
* "r" (abreviação para read) para leitura.

**Exemplo**:
ler_csv = open('arquivo.csv','r')
escrever_csv = open('arquivo.csv','w')

## Nota

    'r': modo de leitura, o arquivo deve existir previamente
    'w': modo de escrita, se o arquivo não existir, ele será criado
    'a': modo de anexar, adiciona informações ao final do arquivo
    'x': modo exclusivo, cria um novo arquivo somente se ele não existir
    'b': modo binário, usado para arquivos binários, como imagens ou vídeos
    't': modo de texto, usado para arquivos de texto


## LENDO UM ARQUIVO
arquivo = open('palavras.txt', 'r').
Diferente do modo "w", abrir um arquivo que não existe no modo "r" não vai criar um arquivo. Se "palavras.txt" não existir, o Python vai lançar o erro FileNotFoundError 

### função read() :
Para ler o arquivo inteiro, utilizamos a função read() .
arquivo = open('palavras.txt', 'r')
arquivo.read()
```python
    arquivo = open('texto.txt', 'r')

    conteudo = arquivo.read()

    print(conteudo)
```
## Escrevendo em um arquivo em Python
```python
    arquivo = open('novo_texto.txt', 'w')
    arquivo.write('Olá, Mundo!')
    arquivo.close()
```
## FECHANDO UM ARQUIVO
### função close()
arquivo.close()

## Manipulando arquivos com o statement with
Além de abrir e fechar arquivos manualmente, Python também oferece uma sintaxe mais conveniente para manipulação de arquivos.
* O statement with é usado para abrir um arquivo e garantir que ele seja fechado corretamente, mesmo em caso de erro.

```python
    with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

* Este exemplo, o arquivo é aberto dentro do bloco with e o conteúdo é lido e armazenado na variável conteudo.

* Ao final do bloco with, o arquivo é automaticamente fechado, mesmo que ocorra uma exceção durante a leitura.

* O statement with é especialmente útil quando manipulamos arquivos grandes ou quando há várias operações a serem realizadas no arquivo.