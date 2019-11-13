#LISTA DE MOTIVAÇÃO 4

#1 - soma de a, b e c

#solução com vetor
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

#==--**--==#

#solução sem vetor
def soma(a, b, c):
    
    if(a == 13):
        a, b, c = 0, 0, 0
    elif(b == 13):
        b, c = 0, 0
    elif(c == 13):
        c = 0
    
    return a + b + c

#
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

print(soma(a, b, c))
      
  
######################################


#2 - alunos e médias
n = int(input("número de alunos: "))

nome = []
p1 = []
p2 = []
media = []
opt = 0
r = 0
soma = 0

for i in range(n):
    print("\nALUNO ", i+1)
    nome.append(input("\nnome do aluno: "))
    p1.append(float(input("nota da pr1: ")))
    p2.append(float(input("nota da pr2: ")))
    
    r = int(input("tem nota optativa? 1 pra sim e 0 pra não: "))
    
    if(r == 1):
        opt = float(input("nota da optativa: "))
        
        if(p1[i] < p2[i] and opt > p1[i]):
            p1[i] = opt
            
        elif(p2[i] < p1[i] and opt > p2[i]):
            p2[i] = opt
            
    media.append((p1[i] + p2[i])/2)
            
#média de cada aluno
for i in range(n):
    soma = soma + media[i]
    
    print("")
    print(nome[i], "- MÉDIA: ", media[i], "\n")
    
#média da turma
print("\na média da turma é: ", soma / n)

#percentual de alunos aprovados e reprovados
ap = 0
rep = 0

for i in range(n):
    if(media[i] >= 5):
        ap = ap + 1
    else:
        rep = rep + 1

print("\npercentual de aprovados: ", (ap / n) * 100, "%")
print("percentual de reprovados: ", (rep / n) * 100, "%")
    

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
