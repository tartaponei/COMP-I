#LISTA DE MOTIVAÇÃO 4

#1 - soma de a, b e c
def soma(num):
    soma = 0
    
    if (num[0] != 13):
        for i in range(3):
            if (num[i] != 13):
                soma = soma + num[i]
        
    return soma

#
n = []

for i in range(3):
    n.append(int(input("numero: ")))

print("\na soma é:", soma(n))            


######################################


#2 - media
import numpy

#def

#
n = int(input("numero de alunos: "))

"""
nome    pr1    pr2    opta(op)  media
0 0     0 1    0 2     0 3       0 4
1 0     1 1    1 2     1 3       1 4
"""
alunos = numpy.zeros(5, n)

for i in range(n): #corre as linhas
    print("ALUNO\n", i)
    alunos[i, 0] = input("nome do aluno: ")
    alunos[i, 1] = int(input("nota da pr1: "))
    alunos[i, 2] = int(input("nota da pr2: "))
    
    r = int(input("tem nota optativa? 1 pra sim e 0 pra não: "))
    if(r == 1):
        alunos[i, 3] = int(input("nota da optativa: "))

print(alunos)
    

###########################


#3 - area do circulo
def area(r):
    return 3.141516*(r**2)
#
r = float(input("raio: "))
print("a área é:", area(r))


###########################


#4 - numeros primos
def primo():
    for n in range(1, 100):
        d = 1
        divisores = 0
        while(d <= n):
            if(n % d == 0):
                divisores = divisores + 1
            d = d + 1
        if(divisores == 2):
            print(n)
#
primo()


############################


#5- reverso
def reverso(n):
    s = str(n)
    return int(s[::-1])

n = int(input("numero: "))
print(reverso(n))


#############################

#6- 
