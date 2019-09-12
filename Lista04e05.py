#LISTA 4:
#4- soma e maior que 20
n1 = float(input("primeiro valor: "))
n2 = float(input("segundo valor: "))

soma = n1 + n2

if(soma > 20):
    print(soma + 8)
else:
    print(soma - 5)
    
    
#5- equação quadrática
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

delta = (b ** 2) - (4 * a * c)

if(delta > 0):
    print("a função possui 2 raízes")
elif(delta == 0):
    print("a função possui 1 raiz")
else:
    print("a função possui nenhuma raiz real")
   
#//
#QUEBRA TOP PRA SEPARAR AS LISTAS
#//

#LISTA 5
#1- soma de 1 a 100
soma = 0

for i in range(0, 101):
    soma = soma + i
    
print(soma)


#2- fatorial
n = int(input("valor: "))
fat = 1

if(n > 1):
  for i in range(1, n + 1):
      fat = fat * i
    
print("o fatorial é", fat)


#3- pares de 100 a 200
pares = 0

for i in range(100, 201):
    if(i % 2 == 0):
        pares = pares + 1
    
print(pares)


#4- contagem de pares
n1 = int(input("primeiro valor: "))
n2 = int(input("segundo valor: "))
pares = 0

if(n2 > n1):
    for i in range(n1, n2 + 1):
        if(i % 2 == 0):
            pares = pares + 1
            
elif(n1 > n2):
    for i in range(n2, n1 + 1):
        if(i % 2 == 0):
            pares = pares + 1
    
print(pares)
