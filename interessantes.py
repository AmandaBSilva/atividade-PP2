import random
from copy import copy

PONTOS = 0

mapa = {
    "2": [["1", "2"]],
    "3": [["1", "3"]],
    "4": [["2", "2"], ["1", "4"]],
    "5": [["1", "5"]],
    "6": [["2", "3"], ["1", "6"]],
    "7": [["1", "7"]],
    "8": [["2", "4"], ["2", "2", "2"], ["1", "8"]],
    "9": [["3", "3"], ["1", "9"]],
}

pesos = [1, 1, 2, 1, 2, 1, 3, 2]


def gerador():
    df = random.choices(list(mapa.keys()), pesos, k=1)[0]
    alg = [
        *random.choice(mapa[df]),
        *['1' for i in range(0, random.randint(0, 2))]
    ]
    return "".join([*alg, df])


def continuar():
    r = input("Deseja continuar? ")
    if r in ["n", "Não", "não", "nao"]:
        print(f"Você fez {PONTOS} pontos")
        return False
    else:
        return True


def pergunta_1():
    global PONTOS
    numero = list(gerador())
    indice = random.randint(0, len(numero)-1)
    falta = copy(numero[indice])
    numero[indice] = "A"
    novo = "".join(numero)
    a = input(f"Seja {novo} um número interessante. Qual é o valor de A? ")
    if a == falta:
        PONTOS = PONTOS + 10
        print("Você acertou!!")
    else:
        PONTOS = PONTOS - 5
        print(f"Você errou. A resposta certa é {falta}")


def pergunta_2():
    global PONTOS
    numero = int(gerador())
    n_1 = random.randint(100, numero)
    n_2 = numero - n_1
    escolha = list(str(n_2))
    indice = random.randint(0, len(escolha)-1)
    falta = copy(escolha[indice])
    escolha[indice] = "A"
    novo = "".join(escolha)
    a = input(f"A soma dos números {n_1} e {novo} é um numero interessante. Qual é o valor de A? ")
    if a == falta:
        PONTOS = PONTOS + 20
        print("Você acertou!!")
    else:
        PONTOS = PONTOS - 5
        print(f"Você errou. A resposta certa é {falta}")


def main():
    cont = True
    print("""Um número inteiro positivo é chamado interessante quando termina
com um algarismo que é igual ao produto de seus demais algarismo. """)
    print("Exemplo:")
    print("326 é interessante pois 3 * 2 = 6")
    print("Obs: Nesse jogo não há números interessantes que terminam com 0 ou 1")
    print("---------------------------------")
    while cont:
        escolha = random.choices([pergunta_1, pergunta_2], weights=[4, 1], k=1)[0]
        escolha()
        cont = continuar()


main()
