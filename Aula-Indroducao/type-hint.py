from pydantic import validate_call

#Sem tipagem
def soma (x,y):
    return x + y

#Com Type Hint
def soma_Type_Hint(x:int,y:int)-> int:
    return x + y

@validate_call
def soma_Pydantic(x:int,y:int)->int:
    return x + y


def main():

    print(soma("10","s"))
    print(soma_Type_Hint("10","amor"))
    print(soma_Pydantic(10,10))

main()