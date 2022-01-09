print(10 * "-*-*")
print("\t\t\t JOGO DE DADOS ")
print(10 * "-*-*")


from random import randint
from time import sleep

resposta = str(input("Você deseja jogar?[S]/[N]")).upper()

while resposta == "S":
    print("\n Jogador está jogando....")
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    j_dado1 = randint(1, 6)
    j_dado2 = randint(1, 6)
    print("\nJogador tirou {} e {} nos dados\n".format(j_dado1, j_dado2))
    print("\n Computaor está jogando....")
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    c_dado1 = randint(1, 6)
    c_dado2 = randint(1, 6)
    print("\nComputador tirou {} e {} nos dados\n".format(c_dado1, c_dado2))
    jogador = j_dado2 + j_dado1
    computador = c_dado1 + c_dado2
    if jogador > computador:
        print("Você ganhou, parabens\n")
    elif jogador == computador:
        print("O jogo empatou")
    else:
        print("O computador venceu")
    resposta = str(input("Você deseja jogar outra vez?[S]/[N]")).upper()






