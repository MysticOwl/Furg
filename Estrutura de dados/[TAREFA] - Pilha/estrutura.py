class Node:
    def __init__(self):
        self.__dado = None
        self.__prox = None
    
    def __repr__(self):
        if self.getProx() == None:
            return str(self.getDado())
        else:
            return str(self.getDado()) + '->' + str(self.getProx())
        
    def getDado(self):
        return self.__dado
    
    def getProx(self):
        return self.__prox
    
    def setDado(self,dado):
        self.__dado = dado
    
    def setProx(self,prox):
        self.__prox = prox

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__size = 0

    def __repr__(self):
        string = ''
        if self.getTopo() == None:
            return 'Pilha vazia'
        else:
            pointer = self.getTopo()
            string += str(pointer.getDado()) + '\n'
            while pointer.getProx() != None:
                pointer = pointer.getProx()
                string += str(pointer.getDado()) + '\n'
        return '\nTopo\n' + str(string) + 'Base'
    
    def getSize(self):
        return self.__size

    def getTopo(self):
        return self.__topo
    
    def setTopo(self, topo):
        self.__topo = topo
    
    def addSize(self):
        self.__size += 1
        return self.__size
    
    def remSize(self):
        self.__size -= 1
        return self.__size

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False           
    
    def insert(self,dado):
        node = Node()
        anterior = self.getTopo()
        node.setProx(anterior)
        node.setDado(dado)
        self.setTopo(node)
        self.addSize()
    
    def remove(self):
        prox = self.getTopo().getProx()
        self.setTopo(prox)
        self.remSize()
    
    def destroy(self):
        while self.getSize() != 0:
            topo = self.getTopo()
            self.setTopo(topo.getProx())
            del topo
            self.remSize()
    
    def topoPilha(self):
        if self.isEmpty():
            return False
        return self.getTopo().getDado()
    
    def comparar(self, pilha):
        if self.getSize() != pilha.getSize():
            return False
        firstPilha = self.getTopo()
        secondPilha = pilha.getTopo()
        for i in range(self.getSize()):
            if firstPilha.getDado() != secondPilha.getDado():
                return False
            firstPilha = firstPilha.getProx()
            secondPilha = secondPilha.getProx()
        return True