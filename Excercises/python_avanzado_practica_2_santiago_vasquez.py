# Universidad San Carlos de Guatemala
# Facultad de Ingeniería
# Escuela de Ciencias y Sistemas
# Python Avanzado
# Practica 2

# Santiago Vásquez Ramírez

# Simularemos una cadena de bloques en la que cada bloque contendrá datos y un hash que se calcula a partir del bloque anterior.

# 1. Crea una clase Block que represente un bloque de la cadena de bloques. Cada bloque debe contener los siguientes atributos:
# • index: El índice del bloque en la cadena.
# • previous_hash: El hash del bloque anterior en la cadena (el primer bloque puede tener un valor nulo).
# • timestamp: La marca de tiempo en la que se crea el bloque.
# • data - transactions: Los datos que se desean almacenar en el bloque.
# • hash: El hash del bloque actual, que se calculará a partir de los demás atributos.

from hashlib import sha256
import json
from time import time

class Block:

    def __init__(self, index, transactions, timestamp, previous_hash, _nonce = 0) -> None:
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = _nonce
        self.hash = ""

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

    def __str__(self) -> str:
        return str({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "nonce": self.nonce
        })

# 2. Crea una clase Blockchain que contendrá una lista de bloques y métodos para agregar nuevos bloques y validar la cadena. La clase debe tener los siguientes métodos:
# • __init__(): Inicializa una cadena de bloques con un bloque génesis (el primer bloque).
# • create_block(data): Crea un nuevo bloque con los datos proporcionados y lo agrega a la cadena.
# • get_last_block(): Devuelve el último bloque en la cadena.
# • is_valid(): Verifica si la cadena de bloques es válida asegurándose de que los hashes coincidan y que los índices estén en orden.

class Blockchain:
    
    __difficulty = 2

    def __init__(self) -> None:
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.__difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def create_genesis_block(self):
        genesis_block = Block(0, [], time(), '0')
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def is_valid_proof(self, block, block_hash) -> bool:
        verification = (block_hash.startswith('0' * self.__difficulty)
                        and block_hash == block.compute_hash())
        return verification

    def add_block(self, block, proof) -> bool:
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):

        if len(self.unconfirmed_transactions) == 0:
            return False

        last_block = self.last_block

        new_block = Block(index = last_block.index+1,
                          transactions = self.unconfirmed_transactions,
                          timestamp = time(),
                          previous_hash = last_block.hash)

        print("Minando.....")
        proof = self.proof_of_work(new_block)

        print("previous_hash:", last_block.hash)
        print("proof:", proof)

        is_valid = self.add_block(block = new_block, proof=proof)

        if not is_valid:
            print("Bloque no fue agregado")
            return False

        print("Bloque agregado con exito.")
        self.unconfirmed_transactions = []
        return True

    def check_chain_validity(self, chain):
        result = True
        previous_hash = '0'
        for block in chain:
            block_hash = block.hash
            block.hash = ""
            if not self.is_valid_proof(block, block_hash) or previous_hash != block.previous_hash:
                result = False
                break
            block.hash, previous_hash = block_hash, block_hash
        return result

# 3. Crea una instancia de la clase Blockchain.
# 4. Agrega varios bloques con diferentes datos a la cadena.
# 5. Valida la cadena de bloques para asegurarte de que todos los bloques sean válidos.

blockchain1 = Blockchain()

genesis_block = blockchain1.last_block
print("Genesis Block:", genesis_block)
print("------> genesis block <------")

blockchain1.add_new_transaction({"wallet": 1, "amount": 100})
blockchain1.add_new_transaction({"wallet": 2, "amount": 110})
blockchain1.add_new_transaction({"wallet": 3, "amount": 120})
blockchain1.add_new_transaction({"wallet": 4, "amount": 120})
blockchain1.add_new_transaction({"wallet": 5, "amount": 120})
print("------> 1st process <------")

unconfirmed_transactions = blockchain1.unconfirmed_transactions
print("Transacciones no confirmadas:", unconfirmed_transactions)
print("------> 1er Proceso <------")

blockchain1.mine()
last_block = blockchain1.last_block
print("Último bloque generado:", last_block)
print("------> 1er Proceso <------")

blockchain2 = blockchain1

print("------> Check Chain Validity <------")
is_valid = blockchain1.check_chain_validity(blockchain2.chain)
print("El resulta es: ", is_valid)
print("------> Check Chain Validity <------")