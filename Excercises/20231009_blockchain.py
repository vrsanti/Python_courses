'''
Las transacciones - Son empaquetadas en los bloques en forma de lote
un bloque puede contener una o más transacciones
los bloques que contienen transacciones se generan y agregan regularmente (periodicamente) a la cadena de bloques.
debdio a que hay muchos bloques, cada bloque debe tener una identificación única
'''

from hashlib import sha256
import json
import time

# Bloque

class Block:
        # constructor (inicializador) para la clase "Block"
        # parametro (index): ID único del bloque
        # parametro (transactions): lista de transacciones
        # parametro (timestamp): hora de generación del bloque
        # parametro (previous_has): hash del bloque anterior en la cadena
        # parametro (nonce): el valor nonce en este punto es nuestra prueba de carga de trabajo
        
    def __init__(self, index, transactions, timestamp, previous_hash, _nonce = 0) -> None:
        self.index = index
        self.transactions = transactions 
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = _nonce
        
    def compute_hash(self):
        """
        Devuelve el hash de la instancia del bloque convirtiendolo primero en una cadena JSON.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
    
class Blockchain:
    difficulty = 2  # dificultad del algoritmo PoW

    def __init__(self):
        """
        Constructor para la clase Blockchain
        """
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Una función para generar un bloque de génesis y lo agrega a
        la cadena. El bloque tiene índice 0, anterior_hash como 0 y
        un hash válido.
        """
        genesis_block = Block(0, [], time.time(), '0')
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        """
        Una forma rápida de recuperar el bloque más reciente de la cadena. Tenga en cuenta que
        a cadena siempre constará de al menos un bloque (es decir, bloque de génesis)
        """
        return self.chain[-1]
        
    def proof_of_work(self, block):
        """
        Funcion que prueba diferentes valores del nonce para obtener un hash
        que satisfaga nuestros criterios de dificultad
        """
        block.nonce = 0
        print("Nonce inicial:", block.nonce)
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        print("Nonce final:", block.nonce)
        return computed_hash

    def is_valid_proof(self, block, block_hash):
        """
        Comprueba si block_hash es un hash de bloque valido y cumple los criterios de dificultad
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())
    
    def add_block(self, block, proof):
        """
        Una función que agrega el bloque a la cadena después de la verificación.
        La verificación incluye:
        * Comprobación de si la prueba es válida.
        * El anterior_hash referido en el bloque y el hash de un último bloque
          en el partido de la cadena.
        """
        previos_hash = self.last_block.hash

        if previos_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True
    
    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        Esta función sirve como interfaz para agregar los pendientes
        transacciones a la cadena de bloques agregándolas al bloque
        y averiguar la prueba de trabajo.
        """

        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index+1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previuos_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        print("Minando")
        print("previous_hash:", last_block.hash)
        print("proof:", proof)

        self.add_block(block=new_block, proof=proof)
        self.unconfirmed_transactions = []
        return new_block.index

    def check_chain_validity(self, chain):
        """
        Un método auxiliar para verificar si toda la cadena de bloques es válida.          
        """
        result = True
        previos_hash = '0'

        # Iterar a traves de toda la cadena
        for block in chain:
            block_hash = block.hash
            # Eliminar el campo hash para volver a calcular el hash nuevamente
            delattr(block, "hash")
            print(block.previous_hash)

            if not self.is_valid_proof(block, block_hash) or previos_hash != block.previous_hash:
                result = False
                break

            block.hash, previos_hash = block_hash, block_hash

        return result