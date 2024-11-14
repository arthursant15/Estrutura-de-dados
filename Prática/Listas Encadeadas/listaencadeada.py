#Codigo identado, porem sem a minha explicação fodastica

# Jeito de adicionar um elemento na lista normal
# sequencial = []
# sequencial.append(10)

# Importe da classe Node do arquivo Nó.py
from node import Node

# Criação da classe LinkedList (Lista encadeada)
class LinkedList:
    # Método construtor que inicializa uma lista vazia.
    def __init__(self):
        # Cabeça vazia
        self.head = None
        # Atributo _size para deixar explícito que não deve ser modificado externamente
        self._size = 0

    def append(self, elem):
        # Caso já tenha valor na cabeça, cria um novo elemento
        if self.head:
            pointer = self.head
            # Continua até o próximo ponteiro ser None
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    # Método que mostra o comprimento total da lista
    def __len__(self):
        return self._size

    # Método para acessar um nó específico pelo índice
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List Index out of range")
        return pointer

    def set(self, index, elem):
        # lista.set(índice, elemento)
        node = self._getnode(index)
        if node:
            node.data = elem
        else:
            raise IndexError("List Index out of range")

    # Método especial __getitem__ para acessar o item pelo índice
    def __getitem__(self, index):
        node = self._getnode(index)
        if node:
            return node.data
        raise IndexError("List Index out of range")

    # Método especial __setitem__ para atribuir o valor pelo índice
    def __setitem__(self, index, elem):
        node = self._getnode(index)
        if node:
            node.data = elem
        else:
            raise IndexError("List Index out of range")

    def index(self, elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} is not in List")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head is None:
            raise ValueError(f"{elem} is not in List")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{elem} is not in List")

    def __repr__(self):
        # Representação da lista para depuração
        elements = []
        pointer = self.head
        while pointer:
            elements.append(str(pointer.data))
            pointer = pointer.next
        return " -> ".join(elements)


if __name__ == '__main__':
    # Criação de uma instância de LinkedList e uso de métodos
    lista = LinkedList()
    lista.append(10)
    print(lista)
