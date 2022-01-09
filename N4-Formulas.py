print("-*-*" *10)
print("-*\t\t    SEJA BEM VINDO \t\t\t  -*")
print("-*-*" *10)


def bhaskara():

    print("Digite os termos da equação, A, B e C:\n")
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))

    from math import sqrt

    x1 = (-b + sqrt((b**2)-4*a*c))/2*a
    x2 = (-b - sqrt((b**2)-4*a*c))/2*a

    if x1 == x2:
        print("A raiz da equação é: {}".format(x1))
    else:
        print("As raízes da equação são: {} e {}".format(x1, x2))


def juros_compostos():

    capital_inicial = float(input("Digite o valor aplicado inicialmente em R$: "))
    juros = float(input("Digite a taxa de juros em % anual: "))
    tempo = float(input("Digite a o tempo de investimento em anos: "))
    Montante = capital_inicial*((1+(juros/100))**tempo)
    print("Você receberá R${:.2f}".format(Montante))


def juros_simples():

    capital_inicial = float(input("Digite o valor aplicado inicialmente em R$: "))
    juros = float(input("Digite a taxa de juros em % anual: "))
    tempo = float(input("Digite a o tempo de investimento em anos: "))
    Montante = capital_inicial*(1+((juros/100)*tempo))
    print("Você receberá R${:.2f}".format(Montante))


def triangulo_equilatero():

    from math import sqrt
    lado = float(input("Digite o lado do triângulo: "))
    altura = (lado * sqrt(3))/2
    area = (altura*lado)/2
    print("A altura é {}, e a área, {}".format(altura, area))


print("\n\t\t\tFÓRMULAS\n")
print("[1] - BHASKARA\n"
      "[2] - JUROS COMPOSTOS\n"
      "[3] - JUROS SIMPLES\n"
      "[4] - TRIÂNGULO EQUILÁTERO\n")

opcao = int(input("Digite a formula desejada: "))

if opcao == 1:
    bhaskara()
elif opcao == 2:
    juros_compostos()
elif opcao == 3:
    juros_simples()
elif opcao == 4:
    triangulo_equilatero()
else:
    print("Você digitou uma opção errada.")
