# Definindo uma interface de boas vindas ao
# programa de fibonacci

print("-*-*" *10)
print("-*\t\t    SEJA BEM VINDO \t\t\t  -*")
print("-*-*" *10)

# Definindo uma função que cria uma sequencia
# tradicional de fibonacci, ou seja, começando
# por 0 e 1


def fibonnaci_tradional():
    t_1 = 0
    t_2 = 1
    n_t = int(input("Quantos termos deseja ver: ")) - 2  # Define número de termos
    print(f"{t_1} -> {t_2}", end=" -> ")
    while n_t != 0:  # Define o terceiro termo através de repetição
        t_3 = t_2 + t_1
        print(f"{t_3}", end=" -> ")
        t_1 = t_2
        t_2 = t_3
        n_t -= 1

# Definindo um fibonacci alternativo, ou seja,
# o usuário escolhe o primeiro e segundo termo


def fibonacci_alternativa():
    t_1 = int(input("Defina o primeiro termo: "))  # Usuário escolhe o primeiro termo
    t_2 = int(input("Defina o segundo termo: "))  # Usuário escolhe o segundo termo
    while t_1 > t_2:
        print("ERRO, O PRIMEIRO TERMO É MAIOR QUE O SEGUNDO.")
        t_1 = int(input("Defina o primeiro termo: "))
        t_2 = int(input("Defina o segundo termo: "))
    n_t = int(input("Quantos termos deseja ver: ")) - 2
    print(f"{t_1} -> {t_2}", end=" -> ")
    while n_t != 0:  # Escolhe o terceiro termo através de repetição
        t_3 = t_2 + t_1
        print(f"{t_3}", end=" -> ")
        t_1 = t_2
        t_2 = t_3
        n_t -= 1

# Final do programa, ou seja, onde o usuário escolhe o fibonacci,
# o programa gera o desejado e é encerrado


print("\n\t\t\tFIBONACCI\n")
print("Existem duas opções: \n")
print("FIBONACCI TRADICIONAL: sequência que\n"
      "começa com 0 e 1, seguindo assim como\n"
      "você desejar\n\n")
print("FIBONACCI ALTERNATIVA: sequência que\n"
      "você escolhe os dois primeiros termos\n"
      "desde que o segundo seja maior ou i-\n"
      "gual ao primeiro.\n\n")

print("[1] - FIBONACCI TRADICIONAL\n"
      "[2] - FIBONACCI ALTERNATIVA\n")

opcao = int(input("Qual a sua opção: "))  # Usuário faz a opção de escolher qual fibonacci deseja visualizar

if opcao == 1:
    fibonnaci_tradional()
else:
    fibonacci_alternativa()







