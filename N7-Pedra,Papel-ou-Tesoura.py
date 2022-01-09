from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")

print("-*" * 20)
print("\t\t PEDRA, PAPEL OU TESOURA?")
print("-*" * 20)

print("-*" * 20)
print("Faça a sua jogada e tente a sorte...")
jogador = int(input("[0] - PEDRA\n"
                   "[1] - PAPEL\n"
                   "[2] - TESOURA\n"
                   "SUA JOGADA: "))
computador = randint(0, 2)

print("-*" * 20)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)

print("-*" * 20)
print("O jogador jogou {}".format(itens[jogador]))
print("O computador jogou {}".format(itens[computador]))
print("-*" * 20)

if jogador == computador:
    print("EMPATE, ambos jogaram {}\n".format(itens[jogador]))
if jogador == 0:
    if computador == 1:
        print("DERROTA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))
    else:
        print("VITÓRIA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))
if jogador == 1:
    if computador == 0:
        print("VITÓRIA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))
    else:
        print("DERROTA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))
if jogador == 2:
    if computador == 0:
        print("DERROTA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))
    else:
        print("VITÓRIA, jogador jogou {} e o computador {}".format(itens[jogador], itens[computador]))

