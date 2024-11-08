### Listas (list)

   * Definição: Uma lista é uma coleção de valores indexada ,ordenada e mutável (podemos modificar os valores). Assim,  cada valor é identificado por um índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e assim por diante.
   
   * Sintaxe: As listas são criadas usando colchetes [ ], e os itens são separados por vírgulas.
   
   * Características:
       * Os elementos têm uma ordem, o que significa que cada item tem uma posição (índice).
        
        *  As listas podem armazenar itens de diferentes tipos, como números, strings e até outras listas.
        
        * São mutáveis, ou seja, podemos adicionar, remover ou modificar seus elementos depois de criadas.
    
### Exemplo

```python
    lista: list = [1,"eu",?]
    lista[1] = "linguagem" 
```

## Somando todos os elementos de uma lista

### Aguçando a induição:
```python
    #Em geral quando pensamos em somar valores de elementos de uma estrutura de dados logo nos vem a mente o uso de laço de repetição 
    soma_notas= 0
    for nota in notas:
        soma_notas += notas
```
### Python existe uma função nativa para isso 

dedicada ao cálculo da soma de todos os elementos de uma lista - a função sum()!
notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0]

soma_das_notas = sum(notas)

## Descobrindo o tamanho de uma lista com a função len()
qtd_de_notas = len(notas)

## Removendo um elemento de uma lista com o método remove()
O metodo remove UM ÚNICO ELEMENTO que recebe como parâmetro o valor que queremos remover de nossa lista.

notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
notas.remove(0)

### Atenção!!
nunca alterar uma lista enquanto se itera sobre ela!
O método remove(), por sua vez, ao apagar um elemento, realoca os outros dentro da lista para que não haja um espaço vazio no lugar onde havia o elemento removido. Quando removemos um elemento da lista, a lista realmente diminui de tamanho!

## Filtrando uma lista utilizando list comprehensions

```python
    notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

notas_validas = [nota for nota in notas if nota > 0]
print(notas_validas)

#Resultdo
[9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
```

## Contando elementos em uma lista com o método count()
```python
qtd_de_setes = notas.count(7.0)
print(qtd_de_setes)
```