from random import randint

print("-*" * 20)
print("\t\t SEJA BEM VINDO(A) AO JOGO")
print("-*" * 20)

decisao = str(input("Você deseja jogar?[S]/[N]")).upper()

p_computador = 0
p_jogador = 0

# Corpo do código: onde o jogador escolhe a sua jogado e o computador
# escolhe aleatoriamente o seu número, logo, o jogo roda através de
# comando sequenciais, possuindo um loop que o usuário controla

while decisao == "S":
    print("-*" * 20)
    print("O computador pensou em um número de 1 a 5, \n"
          "tente adivinhá-lo!")
    computador = randint(1, 5)
    jogador = int(input("\nA sua jogada: "))
    if jogador == computador:
        print("\nVocê acertou!")
        p_jogador += 1
    else:
        print("\nVocê errou!")
        p_computador += 1

    decisao = str(input("\nVocê deseja continuar jogando?[S]/[N]")).upper()

print("Placar final: \n\n"
      "COMPUTADOR {} X {} JOGADOR".format(p_computador, p_jogador))

# Conclusão: jogo bem simples de fazer, com o código sendo bem adaptativo
# podemos inclusive usá-lo para fazer um jogo de par ou ímpar

