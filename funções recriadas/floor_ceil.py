#fazendo a função de módulo eu fiquei pensando sobre as funções math.ceil e math.floor e também fiquei curiosa

#math.ceil
def Teto(y):
    x = str(y)
    
    dig = x.split('.')
    
    n = int(dig[0]) + 1
    
    return n

#math.floor
def Chao(y):
    x = str(y)
    
    dig = x.split('.')
    
    return int(dig[0])

#quebra
a = float(input("digite um número pra arredondar pra cima: "))
b = float(input("digite um número pra arredondar pra baixo: "))

print("")
print(a, "--up-->", Teto(a))
print(b, "--down-->", Chao(b))