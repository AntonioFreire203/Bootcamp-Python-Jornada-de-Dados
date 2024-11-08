from typing import List

#1-Calcular Média de Valores em uma Lista

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

#lista=[10,1.2,1.3,1]

#print(calcular_media(lista))

#2-Filtrar Dados Acima de um Limite

def filtrar_acima_limite(valores: List[float],limite: float ) -> List[float]:
    
    resultado = []
    for valor in valores :
         if valor > limite:
            resultado.append(valor)
    
    return resultado

#valores = [1.2,1.33,2.45,2.36,24,36,15,0]
#filtrar_acima_limite(valores,1.25)

#print(len(filtrar_acima_limite(valores,1.25)))

#3-Contar Valores Únicos em uma Lista

def contar_valores_unicos(valores: List [float],unico:float)-> int :
    cont:int = 0
    for valor in valores:
        if valor == unico:
            cont +=1
    return cont

#print(contar_valores_unicos([1.2, 1.33, 2.45, 2.36, 24, 36, 15, 0, 0, 0], 0))


#4-Converter Celsius para Fahrenheit em uma Lista

def converter_celsius_fahrenheit(temp_celsius:List[float])-> List[float] :

    temp_fahrenheit=[] 
    for temp in temp_celsius :
        temp_fahrenheit.append((9 / 5) * temp + 32)

    return temp_fahrenheit


#print(converter_celsius_fahrenheit([37.5, 13.3, 24.5, 23.6, 24, 36.2, 15, 24.7, 80, 60]))

#Calcular Desvio Padrão de uma Lista

def calcular_desvio_padrao(valores: List[float]) -> float:

    media = sum(valores)/len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)

    return variancia ** 0.5