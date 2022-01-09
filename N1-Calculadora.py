print("-*-*" *10)
print("-*\t\t    SEJA BEM VINDO \t\t\t  -*")
print("-*-*" *10)

n1 = float(input("Escolha seu primeiro número: "))
n2 = float(input("Escolha seu segundo número: "))

print("-*-*" *10)

print("\n\t LISTA DE OPERADORES \t")
print("[1] = Soma")
print("[2] = Subtração")
print("[3] = Multiplicação")
print("[4] = Divisão")
print("[5] = Exponenciação")
print("[6] = Radiciação")

from math import isqrt
operador = 0
while 1 > operador <= 6:
    operador = int(input("\nEscolha seu operador: "))

if operador == 1:
    resultado = n1 + n2
    sigla = "+"
else:
    if operador == 2:
        resultado = n1 - n2
        sigla = "-"
    else:
        if operador == 3:
            resultado = n1 * n2
            sigla = "x"
        else:
            if operador == 4:
                resultado = n1 / n2
                sigla = "/"
            else:
                if operador == 5:
                    resultado = n1 ** n2
                    sigla = "^"
                else:
                    resultado = n1 ** (1/n2)
                    sigla = "Raiz"

print(f"{n1} {sigla} {n2} = {resultado}")

