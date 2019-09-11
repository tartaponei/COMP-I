import math

def distanciaDuasRetas():
	a = int(input("\ndigite o valor de a: "))
	b = int(input("digite o valor de b: "))
	c1 = int(input("digite o valor do primeiro valor de c: "))
	c2 = int(input("digite o valor do segundo c: "))
	
	print("\na equação da primeira reta é", a, "x +", b, "y =",c1)
	
	print("\na equação da segunda reta é", a, "x +", b, "y =",c2)
	
	norma = ((a ** 2) + (b ** 2)) ** 0.5
	
	print("\na distancia da reta à origem é", math.fabs(c1 - c2)/norma)
	
#quebra marota
def distanciaRetaPonto():
	x = int(input("\ncoordenada x do ponto: "))
	y = int(input("\ncoordenada y do ponto: "))
	
	print("o ponto é (", x, ",", y, ")")
	
	a = int(input("\ndigite o valor de a: "))
	b = int(input("digite o valor de b: "))
	c = int(input("digite o valor de c: "))
	
	print("\na equação da reta é", a, "x +", b, "y =",c)
	
	norma = ((a ** 2) + (b ** 2)) ** 0.5
	
	print("\na distancia da reta ao ponto é", math.fabs(c - x - y)/norma)
	
#quebra marota
def distanciaRetaOrigem():
	a = int(input("\ndigite o valor de a: "))
	b = int(input("digite o valor de b: "))
	c = int(input("digite o valor de c: "))
	
	print("\na equação da reta é", a, "x +", b, "y =",c)
	
	norma = ((a ** 2) + (b ** 2)) ** 0.5
	
	print("\na distancia da reta à origem é", math.fabs(c)/norma)

#quebra pra saber onde começa a main
tipo = int(input("vamos calcular distancias pra botar em pratica oq aprendemos em algebra linear 2 com barraguito\n\nescolha que distancia vamos calcular:\n\n1- distancia da reta à origem\n2- distancia da reta a um ponto\n3- distancia entre duas retas\n"))

if(tipo == 1):
	distanciaRetaOrigem()
	
elif(tipo == 2):
	distanciaRetaPonto()
	
elif(tipo == 3):
	distanciaDuasRetas()