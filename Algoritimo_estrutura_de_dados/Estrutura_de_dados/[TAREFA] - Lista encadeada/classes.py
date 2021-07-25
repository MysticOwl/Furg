from typing import List


class Node:
    def __init__(self,data):
        '''Construtor do node'''
        self.data = data
        self.next = None
    
    def __repr__(self):
        '''Representação do node em forma de string'''
        return str(self.data) + ' -> ' + (str(self.next))

class Lista:
    def __init__(self):
        '''Construtor da classe'''
        self.__head = None
        self.__size = 0
    
    def __repr__(self):
        '''Representação da lista em forma de string'''
        return '[' + str(self.__head) + ']'
    
    def getSize(self):
        '''Retorna o tamanho da lista'''
        return self.__size
    
    def getHead(self):
        '''Returna o primeiro elemento da lista'''
        return self.__head
    
    def isEmpty(self):
        '''Verifica se a lista é vazia'''
        if self.__size == 0 or self.getHead() == None:
            return True
        else:
            return False
      
    def addInList(self,index,elem):
        '''Adiciona na posição [i] o elemento [x]'''
        if index == 1 or self.isEmpty():
            node = Node(elem)
            node.next = self.__head
            self.__head = node
        else:
            aux = self._getIndexNode(index-1)
            node = Node(elem)
            node.next = aux.next
            aux.next = node
        self.__size += 1
    
    def removeIn(self,index):
        if self.isEmpty():
            return False
        if index <= 0:
            return False
        aux = self.getItem(index)
        self.removeElem(aux)
        return True
            

    def removeElem(self,elem):
        if self.isEmpty():
            return False
        elif self.__head.data == elem:
            self.__head = self.__head.next
            return True
        else:
            prev = self.__head
            aux = self.__head.next
            while aux != None:
                if aux.data == elem:
                    prev.next = aux.next
                    aux.next = None
                prev = aux
                aux = aux.next
            self.__size -= 1
            return True

    def getItem(self, index):
        '''Retorna o elemento na posição desejada [ i ]'''
        if (1 <= index <= self.getSize()):            
            return self._getIndexNode(index).data
        else:
            return False
    
    def setItem(self,index,elem):
        '''Atribui um elemento posção desejada [ i,var ]'''
        if (1 <= index <= self.getSize()):
            self._getIndexNode(index).data = elem
        else:
            return False

    def _getIndexNode(self,index):
        '''Retorna o elemento na posição desejada [ i ]'''
        if index < 0:
            return False   
        aux = self.__head
        if self.isEmpty():
            return False
        else:
            for i in range(1,index):
                if aux != None:
                    aux = aux.next
                else:
                    return False
        return aux
    
    def search(self, elem):
        '''Procura se existe o elemento na lista [ var ]'''
        aux = self.__head
        i = 1
        if aux.data == elem:
            return('O elemento "{}" se encontra na posição {}'.format(elem,i))
        while aux != None:
            if aux.data == elem:
                return ('O elemento "{}" se encontra na posição {}'.format(elem,i-1))
            else:
                aux = aux.next
                i += 1
        return False
    
    def destroy(self):
        aux = self.__head
        self.__head = None
        aux.next = None
        self.__size = 0
        return True

import random
lista = Lista()
for i in range(10):
    lista.addInList(i,random.randint(1,999))
print(lista)