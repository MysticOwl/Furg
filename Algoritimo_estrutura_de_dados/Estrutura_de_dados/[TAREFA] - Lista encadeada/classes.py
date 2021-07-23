#Construção da classe nodo na para a lista
class Node:
    def __init__(self,dado):
        self.dado = dado
        self.next = None

#Construção da classe lista
class Lista:

#-------------------------------------------------------#
#   Checklist:                                          #
#       Criar uma lista encadeada                       #
#       Inserir na posição | Valor - Posição            #
#       Remover da posição                              #
#       Procurar o valor de acordo com a posição        #
#       Procurar a posição de acordo com o valor        #
#       Destroir a lista                                #
#-------------------------------------------------------#

    def __init__(self,size):

        """Cria uma lista com "size" tamanho."""

        self.__size = size
        self.__array = [0] * size
    
    def getArray(self):

        '''Retorna a lista global.'''

        return self.__array


    def getTamanhoLista(self):

        '''Retorna o tamanho da lista.'''

        return self.__size