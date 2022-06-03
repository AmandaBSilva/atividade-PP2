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


def gerar_numero_interessante() -> str:
    digito = random.choices(list(mapa.keys()), pesos, k=1)[0]
    fatores = [
        *random.choice(mapa[digito]),
        *['1' for i in range(0, random.randint(0, 2))]
    ]
    random.shuffle(fatores)
    return "".join([*fatores, digito])


def continuar() -> bool:
    r = input("Deseja continuar?(n para não, qualquer outra tecla para sim) ")
    if r.lower() == "n":
        print(f"Você fez {PONTOS} pontos")
        return False
    else:
        return True


def verificar_resposta(resposta: str, algarismo: str, pt=20) -> None:
    global PONTOS
    if resposta == algarismo:
        PONTOS += pt
        print("Você acertou!!")
    else:
        PONTOS -= 5
        print(f"Você errou. A resposta certa é {algarismo}")


def ocultar_algarismo(numero: list) -> tuple:
    indice = random.randint(0, len(numero)-1)
    algarismo = copy(numero[indice])
    numero[indice] = "A"
    oculto = "".join(numero)
    return algarismo, oculto


def pergunta_1() -> None:
    interessante = list(gerar_numero_interessante())
    algarismo, oculto = ocultar_algarismo(interessante)
    r = input(f"Seja {oculto} um número interessante. Qual é o valor de A? ")
    verificar_resposta(r, algarismo, 10)


def pergunta_2() -> None:
    interessante = int(gerar_numero_interessante())
    n1 = random.randint(100, interessante)
    n2 = interessante - n1
    algarismo, oculto = ocultar_algarismo(list(str(n2)))
    r = input(f"A soma dos números {n1} e {oculto} é um numero interessante. Qual é o valor de A? ")
    verificar_resposta(r, algarismo)


def pergunta_3() -> None:
    interessante = int(gerar_numero_interessante())
    for n in [2, 3, 5, 7]:
        if interessante % n == 0:
            quociente = interessante//n
            algarismo, oculto = ocultar_algarismo(list(str(quociente)))
            r = input(f"O número {oculto} vezes {n} é igual a um número interessante. Qual é o valor de A? ")
            verificar_resposta(r, algarismo)
            break
    else:
        pergunta_3()


def main() -> None:
    cont = True
    print("""Um número inteiro positivo é chamado interessante quando termina
com um algarismo que é igual ao produto de seus demais algarismo.
Exemplo:
13126 é interessante pois 1* 3 * 1 * 2 = 6.
Obs: Nesse jogo não há números interessantes que terminam com 0 ou 1
""")
    while cont:
        pergunta = random.choices([pergunta_1, pergunta_2, pergunta_3],
                                  weights=[4, 2, 1],
                                  k=1)[0]
        pergunta()
        cont = continuar()
        print("--------------------------------------------------------------")


if __name__ == "__main__":
    main()
