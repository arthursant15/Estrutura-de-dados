# Vamos implementar os seguintes elementos: 
# 1- Inserir na pilha
# 2- Remover da pilha
# 3- Observar o top da pilha

#Importei a classe Node do arquivo Nó.py
from node import Node

#Criei uma classe LinkedList (Lista encadeada)
class Pilha:
    #Metodo construtor que inicializara uma pilha vazia.
    def __init__(self):
        #Com a topo vazia
        self.top = None
        #Para você deixar explicito que não quer que ninguem mexa no atributo, em python se uma a inicialização do atributo com o "_", como vemos em "_size"
        self._size = 0

    def push(self, elem):
        #insere um elemento da pilha 
        # 1- Criei um nó apartir da classe Node
        # 2- A ligação feita com o proximo no com o topo, ou seja o antigo no vai decer uma posição, pois ele recebera o valor que estava no topo antes
        # 3- E por ultimo é atribuido ao topo o novo valor que será adicionado.
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        #remove o elemento do topo da pilha
        # 1- Se o comprimento for maior que 0 então ele ira execultar, senão recebera um erro.
        # 2- O nó vai receber o valor do topo.
        # 3- O valor do topo vai ser jogado pro campo next que será o nada/None
        # 4- Será tirado menos um no comprimento da pilha.
        # 5- Irá retornar o data/dado/valor que está no nó
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A lista está vazia")

    def peek(self):
        #retorna o ultimo elemento do topo da pilha sem o remover
        # 1- Se o comprimento da pilha for maior que 0 então será execultado, senão recebera um erro.
        # 2- Ele irá retornar o dado do topo, caso a informação do If for verdadeiro.
        if self._size > 0:
            return self.top.data
        raise IndexError("A lista está vazia")

    #Aqui eu criei um metodo que mostrara o comprimento total da pilha.
    def __len__(self):
        #Retorna o tamanho da pilha
        return self._size
    
    #Referencia o objeto na hora de ter o output no terminal (print)
    def __repr__(self):
        r = " |"
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "| \n |"
            pointer = pointer.next
        return r
    
    #Como se converte em uma String
    def __str__(self):
        return self.__repr__()
    
#Demonstração do codigo: 
#1- Metodo Push/Adicionar:
pilha = Pilha()
print("-------------------")
print("Metodo Push")
pilha.push(11)
pilha.push(100)
pilha.push(60)
pilha.push(50)
pilha.push(400)
pilha.push(30)
pilha.push(200)
print(pilha)
print("-------------------")
#2- Metodo Pop/Remover
print("Metodo Pop")
pilha.pop()
pilha.pop()
print(pilha)
print("--------------------")
#3- Metodo peek
print("Metodo peek")
pilha.peek()
print("O ultimo valor da pilha vai ser o: {}".format(pilha.peek()))
print("-------------------")
#4- Metodo Len
print("Metodo Len/Comprimento")
print("")
print("O comprimento total da pilha é: {}".format(len(pilha)))