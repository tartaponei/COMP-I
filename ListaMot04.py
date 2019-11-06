#LISTA DE MOTIVAÇÃO 4

#1 - soma de a, b e c
def soma(num):
    soma = 0
    
    if (num[0] != 13):
        for i in range(3):
            if (num[i] != 13):
                soma = soma + num[i]
        
    return soma

#main
n = []

for i in range(3):
    n.append(int(input("numero: ")))

print("\na soma é:", soma(n))            


#2 - media
def

#main
n = int(input("numero de alunos: "))
#socorro nao sei matriz


#3 - area do circulo
def area(r):
    return 3.141516*(r**2)

r = float(input("raio: "))
print("a área é:", area(r))

#4 - numeros primos
def primo():
    for i in range(100):
        for n in range(i):
            if (i % n ):
            print(i)
            
primo()
