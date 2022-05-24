import random
import copy

mapa = {
	2: [[2]],
	3: [[3]],
	4: [[2, 2], [4]],
	5: [[5]],
	6: [[2, 3], [6]],
	7: [[7]],
	8: [[2, 4], [2, 2, 2], [8]],
	9: [[3, 3], [9]],
	}

def gerador():
	df = random.choice(list(mapa.keys()))
	fac = random.choice(mapa[df])
	um = [1 for i in range(0, random.randint(1, 2))]
	numero = "".join([*[str(i) for i in [*fac, *um]], str(df)])
	return  list(numero)

def continuar():
	r = input("Deseja continuar? ")
	if r in ["n", "Não", "não", "nao"]:
		return False
	else:
		return True
		
def pergunta():
	numero = gerador()
	indice = random.randint(0, len(numero)-1)
	falta = copy.copy(numero[indice])
	numero[indice] = "A"
	a = input(f"Seja {"".join(numero)} um número interessante. Qual é o valor de A? ")
	if a == falta:
		print("Você acertou!!")
	else:
		print("Você errou.")
	c = continuar()
	if c:
		pergunta()
	else:
		exit()
		
pergunta()
