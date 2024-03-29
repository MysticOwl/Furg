from pilha_contiguidade import *
from pilha_encadeada import *

class Node:
    def __init__(self):
        self.__dado = None
        self.__prox = None
    
    def __repr__(self):
        return str(self.getDado())
        
    def getDado(self):
        return self.__dado
    
    def getProx(self):
        return self.__prox
    
    def setDado(self,dado):
        self.__dado = dado
    
    def setProx(self,prox):
        self.__prox = prox

def comparaPilhas(pilha1,pilha2):
    if pilha1.getSize() != pilha2.getSize():
        return False
    topo_pilha1 = pilha1.getTopo()
    for i in range(pilha1.getSize()):        
        topo_pilha2 = pilha2.getElem(i)
        if topo_pilha1.getDado() != topo_pilha2:
            return False
        topo_pilha1 = topo_pilha1.getProx()
    return True