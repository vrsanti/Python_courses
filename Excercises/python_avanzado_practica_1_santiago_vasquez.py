# Universidad San Carlos de Guatemala
# Facultad de Ingeniería
# Escuela de Ciencias y Sistemas
# Python Avanzado
# Practica 1

# Santiago Vásquez Ramírez

# Crea una clase llamada Queue que represente una cola. La cola debe tener los siguientes métodos:
#     • __init__(): Un constructor que inicializa una cola vacía.
#     • enqueue(item): Agrega un elemento al final de la cola.
#     • dequeue(): Elimina y devuelve el elemento en la parte frontal de la cola.
#     • is_empty(): Devuelve True si la cola está vacía, False en caso contrario.
#     • size(): Devuelve el número de elementos en la cola.

class queue:

    def __init__(self, size = 1000) -> None:
        self.q = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value) -> None:
        print("Insertando elemento:", value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count += 1

    def dequeue(self) -> None:
        aux = self.q[self.front]
        print("Removiendo elemento:", aux)
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return aux

    def is_empty(self) -> bool:
        return self.count == 0

    def size(self) -> int:
        return self.count

# Con la clase Queue realizar las siguientes operaciones:
#     • Crear una cola vacía.
#     • Agregar los siguientes elementos a la cola: 10, 20, 30, 40, 50.
#     • Imprimir el tamaño de la cola.
#     • Eliminar el elemento en la parte frontal de la cola.
#     • Imprimir el elemento eliminado.
#     • Verificar si la cola está vacía.
#     • Agregar 60 y 70 a la cola.
#     • Imprimir el tamaño de la cola nuevamente.
#     • Eliminar y mostrar todos los elementos de la cola uno por uno.

cola = queue()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

print("Tamaño de la cola:", cola.size())

cola.dequeue()

cola.is_empty()

cola.enqueue(60)
cola.enqueue(70)

print("Tamaño de la cola:", cola.size())

for i in range(cola.size()):
    print(cola.dequeue())