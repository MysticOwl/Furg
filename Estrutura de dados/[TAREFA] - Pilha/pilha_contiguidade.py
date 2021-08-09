class PilhaContiguidade:
    def __init__(self,size):
        self.__vector = [None] * size
        self.__limite = size - 1
        self.__base = 0
        self.__topo = -1
    
    def getSize(self):
        return len(self.__vector)
    
    def __repr__(self):
        string = ''
        pointer = self.getSize()
        if (self.isEmpty()):
            return 'Pilha vazia'
        for i in range(self.__topo + 1):
            pointer -= 1
            string += str(self.__vector[pointer]) + '\n'
        return '\nTopo\n' + str(string) + 'Base'
    
    def isEmpty(self):
        if self.__topo < 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.__topo == self.__limite:
            return True
        else:
            return False
    
    def insert(self,elem):
        if (self.isEmpty()):
            self.__topo += 1
            self.__vector[self.__topo] = elem
        elif (self.isFull()):
            return False
        else:
            self.__topo += 1
            self.__vector[self.__topo] = elem
        
    def remove(self):
        if (self.isEmpty()):
            return False
        else:
            self.__topo -= 1
    
    def destroy(self):
        if (self.isEmpty()):
            return False
        else:
            while self.__topo >= 0:
                del self.__vector[self.__topo]
                self.__topo -= 1
   
    def getTopo(self):
        if (self.isEmpty()):
            return False
        else:
            return self.__vector[self.__topo]
    
    def getElem(self,index):
        if (self.isEmpty()):
            return False
        else:
            pointer = (self.getSize()-1) - index
            return self.__vector[pointer]
    
    def _getVector(self):
        return self.__vector