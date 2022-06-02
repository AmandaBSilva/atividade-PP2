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


def gerador() -> str:
    digito = random.choices(list(mapa.keys()), pesos, k=1)[0]
    fatores = [
        *random.choice(mapa[digito]),
        *['1' for i in range(0, random.randint(0, 2))]
    ]
    random.shuffle(fatores)
    return "".join([*fatores, digito])


def continuar() -> bool:
    r = input("Deseja continuar?(n para não, e qualquer tecla para sim) ")
    if r in ["n", "Não", "não", "nao"]:
        print(f"Você fez {PONTOS} pontos")
        return False
    else:
        return True


def mensagem(a: str, apagado: str, qt=20):
    global PONTOS
    if a == apagado:
        PONTOS += qt
        print("Você acertou!!")
    else:
        PONTOS -= 5
        print(f"Você errou. A resposta certa é {apagado}")


def ocultar(numero: list) -> tuple:
    indice = random.randint(0, len(numero)-1)
    apagado = copy(numero[indice])
    numero[indice] = "A"
    sem_digito = "".join(numero)
    return apagado, sem_digito


def pergunta_1():
    interessante = list(gerador())
    apagado, sem_digito = ocultar(interessante)

    a = input(f"Seja {sem_digito} um número interessante. Qual é o valor de A? ")
    mensagem(a, apagado, 10)


def pergunta_2():
    interessante = int(gerador())
    n_1 = random.randint(100, interessante)
    subtração = list(str(interessante - n_1))
    apagado, sem_digito = ocultar(subtração)

    a = input(f"A soma dos números {n_1} e {sem_digito} é um número interessante. Qual é o valor de A? ")
    mensagem(a, apagado)


def pergunta_3():
    interessante = int(gerador())
    for n in [2, 3, 5, 7]:
        if interessante % n == 0:
            fator = n
            q = list(str(interessante//n))
            apagado, sem_digito = ocultar(q)
            a = input(f"O número {sem_digito} vezes {fator} é igual a um número interessante. Qual é o valor de A? ")
            mensagem(a, apagado)
            break
    else:
        pergunta_3()


def main():
    cont = True
    print(
"""Um número inteiro positivo é chamado interessante quando termina
com um algarismo que é igual ao produto de seus demais algarismo. 
Exemplo:
13126 é interessante pois 1* 3 * 1 * 2 = 6.
Obs: Nesse jogo não há números interessantes que terminam com 0 ou 1
"""
)
    while cont:
        pergunta = random.choices(
            [pergunta_1, pergunta_2, pergunta_3],
            weights=[4, 2, 1],
            k=1
        )[0]
        pergunta()
        cont = continuar()
        print("---------------------------------------")


if __name__ == "__main__":
    main()
