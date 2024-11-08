def dados(nome, idade=None):
    if(idade is not None):
       return ('nome: {} \nidade: {}'.format(nome, idade))
    else:
       return ('nome: {} \nidade: não informada'.format(nome))
    

#print(type(dados('antonio',30)))


def calculadora(x, y):
    return{'soma':x+y,'multiplicação':x*y,'divisão':x/y,'subtração':x-y}

resultados = calculadora(1,2)
    
for key in resultados:
    print('{}:{}'.format(key,resultados[key]))