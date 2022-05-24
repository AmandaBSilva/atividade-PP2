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
	9:[[3, 3], [9]],
	}

def gerador():
	df = random.choice(list(mapa.keys()))
	fac = random.choice(mapa[df])

	uns = random.randint(0, 3)
	um = [1 for i in range(0, random.randint(1, 2))]
	alg = [*fac, *um]
	numero = "".join([*[str(i) for i in alg], str(df)])
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
	novo = "".join(numero)
	a = input(f"Seja {novo} um número interessante. Qual é o valor de A? ")
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
