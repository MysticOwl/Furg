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
    
    def addLast(self,elem):
        '''Adiciona elementos sequencialmente na lista'''
        if self.isEmpty():
            #Insere um node quando a lista for vazia
            elem = Node(elem)
            self.__head = elem
        else:
            #Insere um node sempre na ultima posição
            aux = self.__head
            while(aux.next):
                aux = aux.next
            aux.next = Node(elem)
        self.__size += 1
    
    def addInList(self,index,elem):
        '''Adiciona na posição [i] o elemento [x]'''
        if index == 1:
            node = Node(elem)
            node.next = self.__head
            self.__head = node
        else:
            aux = self._getIndexNode(index)
            node = Node(elem)
            node.next = aux.next
            aux.next = node
        self.__size += 1

    def removeElem(self,elem):
        if self.isEmpty():
            raise ValueError('Elemento não está na lista. Lista vazia')
        elif self.__head.data == elem:
            self.__head = self.__head.next
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

    def getItem(self, index):
        '''Retorna o elemento na posição desejada [ i ]'''
        aux = self._getIndexNode(index)
        if aux != None:
            return aux.data
        else:
            raise IndexError('Indice fora da lista')
    
    def setItem(self,index,elem):
        '''Atribui um elemento posção desejada [ i,var ]'''
        aux = self._getIndexNode(index)
        if aux != None:
            aux.data = elem
        else:
            raise IndexError('Indice fora da lista')

    def _getIndexNode(self,index):
        '''Retorna o elemento na posição desejada [ i ]'''
        if index <= 0:
            raise IndexError('Indice fora da lista')
        aux = self.__head
        if self.isEmpty():
            raise IndexError('A lista está vazia')
        else:
            for i in range(1,index):
                if aux != None:
                    aux = aux.next
                else:
                    raise IndexError('Indice fora da lista.')
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
        raise ValueError('O elemento {} não se encontra nessa lista'.format(elem))
    
    def destroy(self):
        aux = self.__head
        self.__head = None
        aux.next = None
        return True