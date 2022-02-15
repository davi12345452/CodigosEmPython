from Blockchain import Blockchain


b1 = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
b2 = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
b3 = {"sender": "Cole", "receiver": "Alice", "amount": "35"}
b4 = {"sender": "Alice", "receiver": "Bob", "amount": "10"}
b5 = {"sender": "Bob", "receiver": "Cole", "amount": "5"}
b6 = {"sender": "Cole", "receiver": "Alice", "amount": "70"}
b7 = {"sender": "Alice", "receiver": "Bob", "amount": "500"}
b8 = {"sender": "Bob", "receiver": "Cole", "amount": "85"}
b9 = {"sender": "Cole", "receiver": "Alice", "amount": "23"}

lista_de_blocos = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

block_chain = Blockchain()

for elem in lista_de_blocos:
    block_chain.add_block(elem)

cont = 0
for elem in block_chain.chain:
    print(f"Hash Bloco {cont}: {elem}")
    cont += 1
