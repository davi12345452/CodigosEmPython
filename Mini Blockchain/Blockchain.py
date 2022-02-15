from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = list()
        self.bloco_genesis()

    def bloco_genesis(self):
        trans = dict()
        hash_ant = "0000"
        self.chain.append(Block(hash_ant, trans).hash)

    def add_block(self, trans):
        bloco_novo = Block(self.chain[-1], trans)
        self.chain.append(bloco_novo.hash)
        return bloco_novo



