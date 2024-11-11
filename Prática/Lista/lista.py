#Definindo lista

# 1-Fazemos uma função em que tem como parametro a lista e o elemento em que você deseja encontrar na lista

def busca (lista,elem): 
    
    # ultilizaremos o for para fazermos a busca pela lista.
    # range(len(lista)) = ira verificar até o tamanho da lista.
    for i in range(len(lista)):

        # ultilizamos o if para verificarmos se é o elemento em questão, caso ele for irá retornar i que seria o indice da lista.
        if lista[i] == elem:
            return i    
        # None é uma propriedade em python que quer dizer nada ou nenhum.
    return None
    
funcao_estranha = [10,82,"Arthur", 44, "Idolino"]
elemento = "Idolino"

indice = busca(funcao_estranha, elemento)

if indice is not None:
    print("O indice do elemento {} é o {}. ".format(elemento,indice))
else:
    print("O elemento {} não se encontra na lista.".format(elemento))