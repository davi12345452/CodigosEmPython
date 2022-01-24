# Array que será formado de 0 e 1, o valor 1 será
# quando a linha = coluna, e o restante = 0

array = []
largura = 100
tamanho = 10

for altura in range(tamanho):
    for linha in range(largura):
        if linha >= 10 * altura:
            print(1, end="")
        else:
            print(0, end="")
    print("")

