#Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos,
#o desafio consiste em ler os dados, processá-los em um dicionário para análise 
# e, por fim, calcular e reportar as vendas totais por categoria de produto



import csv
from typing import List, Dict

##Ler CSV

def ler_arquivo_csv(arquivo: str) -> List[Dict[str,str]]:
    with open('vendas.csv',mode="r",encoding='utf-8') as arquivo :
                dados_vendas = csv.DictReader(arquivo)
                return list(dados_vendas)   

#[{'Produto': 'Notebook', 'Categoria': 'Electronics', 'Quantidade': '5', 'Venda': '3000'},...]

# Função para processar os dados em um dicionário
def processar_dados(dados: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

#{'Electronics': 
# [{'Produto': 'Notebook', 'Categoria': 'Electronics', 'Quantidade': '5', 'Venda': '3000'},
# {'Produto': 'Smartphone', 'Categoria': 'Electronics', 'Quantidade': '10', 'Venda': '500'}, 
# {'Produto': 'Tablet', 'Categoria': 'Electronics', 'Quantidade': '2', 'Venda': '1500'}]

#Calcular Vendas por Categoria

def calcular_vendas_categoria(dados: Dict[str, List[Dict[str,str]]])-> Dict[str,int]:
    vendas_por_categoria = {}
    for categoria,itens in dados.items():
         total_vendas = sum(int(item['Quantidade'])*int(item['Venda'])for item in itens)
         vendas_por_categoria[categoria] = total_vendas

    return vendas_por_categoria

def main():
    
    arquivo = 'vendas.csv'
    
    list_dict=ler_arquivo_csv(arquivo)

    dict_list = processar_dados(list_dict)

    vendas_categoria = calcular_vendas_categoria(dict_list)

    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')
    


if __name__ == '__main__':
       main()   