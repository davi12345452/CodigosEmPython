from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, hash_anterior, transacoes):
        self.hash_anterior = hash_anterior
        self.transacoes = transacoes
        self.timestamp = datetime.now()
        self.hash = self.cria_hash()
        print(self.print_bloco())

    def print_bloco(self):
        print("Hash anterior: ", self.hash_anterior)
        print("Transações: ", self.transacoes)
        print("Horário: ", self.timestamp)
        print("Hash do bloco: ", self.hash)
        print("\n")

    def cria_hash(self):
        hash_string = (str(self.hash_anterior) +
                       str(self.transacoes) +
                       str(self.timestamp))
        hash_final = sha256(hash_string.encode())
        return hash_final.hexdigest()



