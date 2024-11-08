
def dados(nome=None,idade=None):
    print('nome:{}'.format(nome))
    if(idade is not None):
        print('idade: {}'.format(idade))
    else:    
        print('idade: não informada ') 


#teste 01
#dados('antonio',20)

#teste 02
#dados('antonio')

#teste 03
#Nossa intenção era passar o número 20 como idade , mas o interpretador vai entender que estamos passando o nome porque não avisamos isso à ele


dados(idade=20)