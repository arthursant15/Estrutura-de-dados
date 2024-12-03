# Vamos implementar os seguintes elementos: 
# 1- Inserir na fila
# 2- Remover da fila
# 3- Observar o top da fila

#Importei a classe Node do arquivo Nó.py
from node import Node

#Criei uma classe LinkedList (Lista encadeada)
class Queue:
    #Metodo construtor que inicializara uma Fila vazia.
    def __init__(self):
        #Foi criada três objetos sendo eles: primeiro elem., ultimo elem. e o tamanho que está privado para não ser acessado.
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None: 
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        #Remover o primeiro elemento da fila
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia")
    
    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")
    #Aqui eu criei um metodo que mostrara o comprimento total da fila.
    def __len__(self):
        #Retorna o tamanho da pilha
        return self._size
    
    #Referencia o objeto na hora de ter o output no terminal (print)
    def __repr__(self):
        if self._size > 0: 
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"
    #Como se converte em uma String
    def __str__(self):
        return self.__repr__()
    
#Demonstração do codigo: 

#1- Demonstração de fila vazia: 
fila = Queue()
print("|    Fila vazia   |")
print(fila)
print("-------------------")

#2- Demontração de adicionar elemento na fila:
fila.push(19)
fila.push(120)

print("|    Adicionar   |")
print(fila)
print("------------------")

#3- Demonstração de remover: 
fila.pop()
print("|    Remover     |")
print(fila)
print("------------------")

#4- Comprimento da fila: 
print("|    Tamanho da fila     |")
print(len(fila))