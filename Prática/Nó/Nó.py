# Explicação do codigo:
# Esse codigo terá como principal função a construção de um nó (Sua definição se encontra nos arquivos do repositório, Anotações/Nó)
# É criado primeiramente uma classe Node que siginifica nó em português
# Depois é criado um metodo construtor que irá construir o objeto 
# Já dentro das instrucões do metodo ocorrerá o seguinte, self é usado justo com data, em português dado, irá receber o parametro data.
# E depois será criado mais um atributo chamado next, que estará apontado para None (Vazio).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None