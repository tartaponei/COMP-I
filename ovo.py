ovo = False
frigideira = False
#oleo = False
#manteiga = False
fogao = False
gas = False

resp = " "

resp = input("vamo fritar um ovo\nresponda sim ou nao\ntem ovo na casa? ")

if (resp == "nao"):
	while (resp == "nao"):
		resp = input("entao vc vai na granja e espera a galinha botar a porra de um ovo\ntem um ovo agora? ")
				
if (resp != "sim" and resp != "nao"):
			print("responde direito, porra")
	
if (resp == "sim"):
	ovo = True
	print("\nagora vc tem o ovo\n\n")
	
	resp = input("tem frigideira na casa? ")
	
	if (resp == "nao"):
		while (resp == "nao"):
			resp = input("vai fritar ovo onde, na mao? vai comprar e depois volta\ntem frigideira agora?")
			
			if (resp != "sim" and resp != "nao"):
				print("responde direito, porra")
		
if (resp == "sim"):
	frigideira = True
	print("\nagora vc tem a frigideira\nvc coloca o ovo na frigideira\n\n")
		
	resp = input("tem fogao? ")
		
	if (resp == "nao"):
		while (resp == "nao"):
			resp = input("vai fazer o ovo onde, na fogueira? vai cair tua mao de tanto segurar o bagulho. arranja um fogao e depois volta\ntem fogao agora? ")
				
		if (resp != "sim" and resp != "nao"):
				print("responde direito, porra")
			
if (resp == "sim"):
	fogao = True
	boca = int(input("\nagora vc tem o fogao\nvc pega a frigideira com o ovo e coloca em uma das bocas do fogao\nescolhe qual boca: 1, 2, 3 ou 4: "))
	
	if(boca < 1 or boca > 4):
		while(boca < 1 or boca > 4):
			boca = int(input("ta inventando boca pro fogao, escolhe direito, porra\nescolhe de novo: "))
	
	print("\n\nvc colocou a frigideira na boca numero", boca)
		
	resp = input("\nquer acender o fogo agora?")
	
	if(resp == "nao"):
		print("\nta esperando oq pra acender? jesus voltar?\nvou tentar acender mesmo assim\n~tenta acender~")
		
	elif(resp != "nao" and resp != "sim"):
		print("responde direito")
		
	resp = input("\n~tenta acender~\nparece que nao tem gás, mas, felizmente, vc foi visitado pela capivara da supergasbras. diga 'ola capivara' e vc recebera um botijao novo de gás: ")
	
	if(resp != "ola capivara"):
		while(resp != "ola capivara"):
			resp = input("\nque falta de respeito com a capivara. diga as palavras magicas: ")
	
if(resp == "ola capivara"):
	gas = True
	tem = int(input("\n\nagora vc conseguiu o gás e podemos acender o fogo\n\nagora escolha quantos minutos devemos deixar o ovo fritando: "))
	
	if(tem < 3):
		print("\né muito pouco tempo, mas vc que manda né")
		coz = 0
		
	elif(tem > 8):
		print("\é tempo demais, mas ok")
		coz = 1
		
	else:
		print("\ntop demais, tempo bom")
		coz = 2
		
	print("\n\n~deixa fritando\n\n")
	
	resp = int(input("agora escolhe um desses utensilhos pra poder dar uma mexida no ovo e botar ele no prato depois (digitar o numero):\n   -1. colher\n   -2. garfo\n   -3. espatula\n   -4. faca\n"))
	
	if(resp == 4):
		print("\npegar ovo com faca? tu é maluco?\nteu ovo caiu no chão antes de chegar no prato\nPARABENS :)")

	if(resp == 1 or resp == 2):
		print("\n\nmeio dificil mas da pra pegar\n\n~mexendo ovo~\n\n~pegando e colocando no prato, misericordia quase caiu~")
		
	if(resp != 4):		
		if(coz == 0):
			print("\n\nseu ovo foi cozido por", tem, "minutos e ficou cru\nPARABENS :)")
	
		elif(coz == 2):
			print("\n\nSEU OVO FICOU PERFEITO, PARABEEEENS :)))))))")
			
		else:
			print("\n\nseu ovo foi cozido por ", tem, "minutos e ficou queimado\nPARABENS :)")