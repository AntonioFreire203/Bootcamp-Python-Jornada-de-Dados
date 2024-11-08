# Funções em Python

## O que é uma função?
uma função é uma
sequência de instruções que computa um ou mais resultados que chamamos de parâmetros . De maneira geral, uma função é um estrutura para agrupar um conjunto de instruções que podem ser
reutilizadas.


## Motivação
A principal motivação para usar funções em Python é a reutilização de código. Funções permitem que você escreva um bloco de código uma vez e o execute múltiplas vezes, possivelmente com diferentes argumentos, para produzir diferentes resultados. Isso ajuda a tornar o código mais legível, modular, e fácil de debugar.


## Definindo Funções
Para criar uma função em Python, você usa a keyword def, seguida de um nome de função, parênteses () contendo zero ou mais "parâmetros", e dois pontos :. O bloco de código indentado que segue é o corpo da função.

    def minha_funcao():
    return "Hello, World!"

## PARÂMETROS DE FUNÇÃO
conjunto de parâmetros consiste em uma lista com nenhum ou mais elementos que podem ser
obrigatórios ou opcionais. Para um parâmetro ser opcional mesmo é atribuído a um valor padrão(default)- None .o None tirar a obrigatoriedade de passar um valor para aquele parametro .Exemplo :

    def dados(nome,idade=None):
        print('nome:{}'.format(nome))
        if(idade is not None):
            print('idade: {}'.format(idade))
        print('idade: não informada ')    


## FUNÇÃO COM RETORNO
Para conseguirmos este comportamento, precisamos que nossa função retorne o valor calculado por
ela. Em Python e em outras linguagens de programação, isto é alcançado através do comando return:
    def dados(nome, idade=None):
        if(idade is not None):
            return ('nome: {} \nidade: {}'.format(nome, idade))
        else:
            return ('nome: {} \nidade: não informada'.format(nome))


### RETORNANDO MÚLTIPLOS VALORES

Apesar de uma função executar apenas um retorno, em Python podemos retornar mais de um valor.

        def calculadora(x, y):
            return x+y, x-y

        print(calculadora(1, 2))

        #retorno, a função devolve uma tupla.

        def calculadora(x, y):
            return {'soma':x+y, 'subtração':x-y}
        resultados = calculadora(1, 2)
            for key in resultados:
                print('{}: {}'.format(key, resultados[key]))

## NÚMERO ARBITRÁRIO DE PARÂMETROS (*ARGS)
Podemos passar um número arbitrário de parâmetros em uma função. Utilizamos as chamadas
variáveis mágicas do Python: *args e **kwargs. utilizar exatamente estes nomes: *args e **kwargs . Apenas o asterisco(*), ou dois deles(**), serão necessários
