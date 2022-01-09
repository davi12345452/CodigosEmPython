print("-*-*" *10)
print("-*\t\t    SEJA BEM VINDO \t\t\t  -*")
print("-*-*" *10)

print("PA ou PG? ")
print("[1] -Progressão Aritmética")
print("[2] -Progressão Geométrica")

operador = 0
while 1 > operador <= 2:
    operador = int(input("Escolha seu operador:"))

numero = int(input("Escolha quantos termos da sequência deseja ver: "))
razao = float(input("Escolha a razão da progressão escolhida: "))
inicial = float(input("Escolha o termo inicial: "))

termo = inicial
i = 0

if operador == 1:
    print(f"\nA PA de razão {razao} e termo inicial {inicial} é: \n\n")
    while numero != 0:
        print(f"{termo}", end="-> ")
        termo += razao
        numero -= 1
    print("\n\n")

elif operador == 2:
    print(f"\nA PG de razão {razao} e termo inicial {inicial} é: \n\n")
    while numero != 0:
        print(f"{termo}", end="-> ")
        termo = inicial*(razao ** i)
        numero -= 1
        i += 1
    print("\n\n")
