#Meu codigo sem identação, mas com explicação do mesmo

#Jeito de adicionar um elemento na lista normal
#sequencial = []
#sequencial.append(10)

#Importei a classe Node do arquivo Nó.py
from node import Node

#Criei uma classe LinkedList (Lista encadeada)
class LinkedList:
    #Metodo construtor que inicializara uma lista vazia.
    def __init__(self):
        #Com a cabeça vazia
        self.head = None
        #Para você deixar explicito que não quer que ninguem mexa no atributo, em python se uma a inicialização do atributo com o "_", como vemos em "_size"
        self._size = 0

    def append(self,elem):
        #Se tiver valor na cabeça então para criar um outro elemento ele vai fazer o seguinte:
        if self.head:
            #Vai criar uma variavel de referencia chamada pointe(ponteiro) que recebera o valor de head
            pointer = self.head
            #Enquanto proximo ponteiro for falso ele ira execultar o bloco de codigo a baixo
            while (pointer.next):
                #A variavel ponteiro vai receber o proximo valor do ponteiro
                pointer = pointer.next
                #E o laço só ira terminar quando a condição a cima for verdadeira ou seja quando o proximo ponteiro for None.
                #Ele ira criar um proximo ponteiro e ele receberá um nó e como parametro para adicionar um elemento
            pointer.next = Node(elem)
        #Se não crie na cabeça um nó e que terá que adicionar um elemento de paramêtro
        else:
            #primeira inserção/adição de elementos
            self.head = Node(elem)
        #Aqui ele ira adicionar mais um toda vez quando se criar um elemento novo.
        self._size = self._size + 1

    
    #Aqui eu criei um metodo que mostrara o comprimento total da lita.
    def __len__(self):
        #Retorna o tamanho da lista
        return self._size
    
    #Aqui a baixo se faz como no java, cria-se o get e o set ambos com as mesmas funções.
    #Esses set e get como metodo não seram ultilizados no codigo, pois será usado como exemplo, caso eu está querendo fazer eles em uma outra linguagem que não tenha a função de sobrecarga de operadores, vista em POO e é só colocar o codigo do mesmo jeito em que se encontra os metodos especiais abaixo.
    def _getnode(self,index):
        #a = lista.get(9)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List Index out of range")
        return pointer
    
    def set(self,index,elem):
        #lista.set(9,7)
        #lista(Indice, elemento)
        pass
    #Aqui é usada a palavra reservada __getitem__ para o metodo ser especial e recebera o parametro index(Começando por 0)
    def __getitem__(self, index):
        #a = lista[10]
        #O ponteiro vai receber o valor do proximo ponteiro, para justamente andar com o ponteiro
        pointer = self._getnode(index)
        #Se o pointer não for none, ou seja ele tem um valor, então o poiter será direcionado ao proximo valor
        if pointer:
            pointer = pointer.next
        #Se o pointer não tiver um valor então gerará essa mensagem "List Index out of range".
        else:
            raise IndexError("List Index out of range")
        #Essa outra condição é realizada para ter certeza, caso o ponteiro tiver um valor então será retornado o valor do mesmo, senão ele irá retornar um erro.
        if pointer:
            return pointer.data
        raise IndexError("List Index out of range")
    
    def __setitem__(self,index, elem):
        #lista[5] = 9
        #O metodo set é a mesma coisa do metodo get (então só irei copia-lo e não irei explica-lo, pois a mesma está a cima)
        pointer = pointer.next
        if pointer:
            pointer = pointer.next
        else:
            raise IndexError("List Index out of range")
        #A unica diferença aqui é que o set ele quer modificar o elemento presente no poiter e não retorna-lo, por isso é atribuido ao valor elem ao em vez de simplismente retornar e tambem se é acresentado um else.
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List Index out of range")
    
    def index(self,elem):
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in List".format(elem))
    
    def insert(self,index,elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size =+1
    
    def remove(self,elem):
        #Caso a cabeça esteja vazia, então ira gerar uma mensagem de erro.
        if self.head == None:
            raise ValueError("{} is not in List".format(elem))
        #Para remover o elemento de uma lista com somente o valor da cabeça basta apontar esse valor para o proximo e assim ira perder a ligação com a cabeça, fazendo o remover.
        elif self.head.data == elem: 
            self.head = self.head.next
            self._size =-1
            return True
        else:
            #O antecessor vai receber um valor inicial da cabeça
            ancestor = self.head
            #O ponteiro vai receber o proximo da cabeça
            pointer = self.head.next
            while(pointer):
                #Se o dado do ponteiro for o elemento que voce quer remover entao ele vai execultar essas duas intruções.
                if pointer.data == elem:
                    #remove, ele ligou o antessesor com o sucessor do nó que queremos remover
                    ancestor.next = pointer.next
                    #Para ter certeza que não esteja levando ninguem, ele é apontado para o vazio
                    self._size =-1
                    return True
                ancestor = pointer
                #Avançar
                pointer = pointer.next
        raise ValueError("{} is not in List".format(elem))
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
    

if __name__ == '__main__':
#Criei uma variavel que recebera a classe Linked e seus metodos.
    lista = LinkedList()
    lista.append(10)
    lista.append(51)
    lista.index(10)
    lista.remove(51)
    lista.append(100)
    lista.append(123)
    lista.append(123)
    lista.append(121)
    lista.append(134)
    lista.append(121)
    lista.append(126)
    print(lista)
    print(lista._size)