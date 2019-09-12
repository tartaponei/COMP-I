#fiquei pensando em como a função math.fabs funcionava, então fiz isso
def calcularModulo(y):
    x = str(y)
    
    if(x.count('-') == 1):
        num = x.split('-')
        
        if(isinstance(y, int)):
            mod = int(num[1])
            return mod
        else:
            mod = float(num[1])
            return mod
    else:
        return x

#quebra
ni = int(input("digite o número inteiro: "))
nf = float(input("digite o número real: "))

print("\no módulo de", ni, "é", calcularModulo(ni))
print("o módulo de", nf, "é", calcularModulo(nf))