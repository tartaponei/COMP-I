#1 - 3, 6, 10, 17, 28


#2 - ler 5 números e informar o maior
numeros = []
for i in range(0,5):
    numeros.append(float(input('Digite um número')))

numeros.sort()
print(numeros[4])


#3- soma dos quadrados
n = int(input("valor: "))
soma = 0

if(n > 0):
	for i in range(1, n+1):
		soma = soma +(i**2)
		
print(soma)


#4- o código dá erro por questão de caracter
#com o caracter correto, sairia 18, 19, 21, 15


#5- fibonacci
n = int(input("numero de termos: "))

atual, anterior = 0, 1
i = 0
while (i < n):
	atual, anterior = anterior, atual + anterior
	print(atual)
	i = i + 1
    
 
#6 - celsius pra fahrenheit
celcius = float(input('Digite a temperatura em celcius'))

trans_fahr = ( celcius * 9/5) + 32 
print('A temperatura correspondente em graus fahreinheit é', trans_fahr )
	

#7- ler 3 n e mostrar em ordem decrescente
n = [0, 0, 0]

for i in range(0, 3):
	n[i] = float(input("numero: "))
	
maior = n[0]
menor = n[0]
meio = n[0]

for i in range(1, 3):
	if(n[i] > maior):
		maior = n[i]

for i in range(1, 3):
	if(n[i] < menor):
		menor = n[i]
		
for i in range(1, 3):
	if(n[i] != maior and n[i] != menor):
		meio = n[i]
	
print(maior, meio, menor)


#8 - triângulo
lados = []
for i in range (0,3):
    lados.append(float(input('Digite um lado para o triangulo')))

if  lados[0] == lados[1] and lados[1] == lados [2]:
    print('O triangulo é um triangulo equilatero')
elif  lados[0] != lados[1] and lados[1] != lados[2] and lados[0] != lados[2]:
    print('O triangulo é um triangulo escaleno')
elif lados[0] == lados[1] and lados[0] != lados[2]:
    print('O triangulo é isocesles')
elif lados[1] == lados[2] and lados[0] != lados[1]:
    print('O triangulo é isosceles')
elif lados[2] == lados[0] and lados[2] != lados[1]:
    print('O triangulo é isosceles')


#9 - o código não imprime nada porque o vetor dias_da_semana não foi especficado
#caso tivesse sido especificado com os dias da semana, imprimiria:
#Hoje é domingo
#   Durmi até tarde
#Hoje é segunda
#   Vou ao trabalho
#Hoje é terça
#   Vou ao trabalho
#Hoje é quarta
#   Vou ao trabalho
#Hoje é quinta
#   Vou ao trabalho
#Hoje é sexta
#   Vou ao trabalho
#Hoje é sábado
#   Dia de dormir tarde...
    
    
#10 - números primos
numero = int(input('Digite um número'))
 
def eh_primo(n):
    if(n < 3): 
        return True
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
        
for i in range (1,numero):
    if(eh_primo(i)):
        print(i)


#11 - [1, 2, 3, 4, 5, 4, 5, 6]


#13 - [2, 9, 1, 0]
            
            
#14        
s, c = 0,1
while c < 7:
    d = 4
    while d > 0:
        s = s + c + d
        d = d – 1
        c = c + 1
print(s)
#a) nada porque o código dá erro por causa de caracter
#caso estivesse com o caracter correto, imprimiria 56

#b)
s = 0
for c in range (1,7):
    for d in range (4,0,-1):
        s = s +  c + d 
print(s)

#resposta 144
            