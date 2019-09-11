#1-"Conceito B", "Conceito C", "Conceito D"


#2- "Aluno não cadastrado"


#3- imprimir soma de dois n
n1 = float(input("primeiro número: "))
n2 = float(input("segundo número: "))

print("\na soma é", n1 + n2)


#4- média de 4 notas
nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
nota3 = float(input("terceira nota: "))
nota4 = float(input("quarta nota: "))

print("\na média é", (nota1 + nota2 + nota3 + nota4) / 4)


#5- maior valor
a = float(input("primeiro valor: "))
b = float(input("segundo valor: "))

if(a > b):
    print("\no maior é", a)
elif(b > a):
    print("\no maior é", b)
else:
    print("\nos dois números são iguais")
    
    
#6- vogal ou consoante
letra = input("digite a letra: ")

if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("\na letra digitada é uma vogal")
else:
    print("\na letra digitada é uma consoante")
    
    
#7- soma e média
num1 = float(input("primeiro número: "))
num2 = float(input("segundo número: "))
num3 = float(input("terceiro número: "))
num4 = float(input("quarto número: "))
num5 = float(input("quinto número: "))

soma = num1 + num2 + num3 + num4 + num5

print("\na soma é", soma)
print("a média é", soma / 5)


#8- números ímpares
for i in range(1, 50, 2):
    print(i)
    
    
#9- potência
base = float(input("valor da base: "))
expoente = float(input("valor do expoente: "))

print("\no resultado é", base ** expoente)


#10- quantidade de pares e ímpares
#só de pensar em fazer isso sem vetor eu já choro
par = 0
impar = 0

v1 = int(input("primeiro valor: "))
if(v1 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v2 = int(input("segundo valor: "))
if(v2 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v3 = int(input("terceiro valor: "))
if(v3 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v4 = int(input("quarto valor: "))
if(v4 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v5 = int(input("quinto valor: "))
if(v5 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v6 = int(input("sexto valor: "))
if(v6 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v7 = int(input("sétimo valor: "))
if(v7 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v8 = int(input("oitavo valor: "))
if(v8 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v9 = int(input("nono valor: "))
if(v9 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
v10 = int(input("décimo valor: "))
if(v10 % 2 == 0):
    par = par + 1
else:
    impar = impar + 1
    
print("\no número de pares é", par)
print("o número de ímpares é", impar)
