from hashlib import sha256
import time


def codigo(texto):
    return sha256(texto.encode("ascii")).hexdigest()


def mineracao(num_bloco, transacoes, hash_anterior, quan_zero):
    n = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(n)
        meu_hash = codigo(texto)
        if meu_hash.startswith("0" * quan_zero):
            return n, meu_hash
        n += 1


if __name__ == "__main__":
    n_bloco = 15
    tran = """
        Davi->Alon->10
        Alon->Joao->50
        Joao->Tomas->11"""
    q_zero = 10
    hash_ant = "aqc"
    resultado = mineracao(n_bloco, tran, hash_ant, q_zero)
    print(resultado)
