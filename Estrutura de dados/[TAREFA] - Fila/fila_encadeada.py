from modulo import *
from pilha_encadeada import*

class Fila:
    def __init__(self):
        self.__ini = None
        self.__fim = None
    
    def getIni(self):
        return self.__ini

    def getFim(self):
        return self.__fim
    
    def setIni(self, elem):
        self.__ini = elem
    
    def setFim(self, elem):
        self.__fim = elem
    
    def __repr__(self):
        string = ''
        pointer = self.getIni()
        if self.getIni() == None:
            return False
        while pointer.getProx() != None:            
            string += str(pointer.getDado()) + '->'
            pointer = pointer.getProx()
        string += str(pointer.getDado())
        return string

    def isEmpty(self):
        if self.getIni() == None and self.getFim() == None:
            return True
        else:
            return False
    
    def insert(self,elem):
        dado = Node()
        if (self.isEmpty()):
            dado.setDado(elem)
            self.setIni(dado)
            self.setFim(dado)
        else:
            dado.setDado(elem)
            self.getFim().setProx(dado)
            self.setFim(self.getFim().getProx())
    
    def remove(self):
        if (self.isEmpty()):
            return False
        elif self.getIni() == self.getFim():
            self.setIni(None)
            self.setFim(None)
        else:
            self.setIni(self.getIni().getProx())
    
    def destroy(self):
        while (not self.isEmpty()):
            self.remove()
    
    def sort(self):
        pilha_ordenada = PilhaEncadeada()
        pilha_auxiliar = PilhaEncadeada()
        while self.getIni() != None:
            if pilha_ordenada.getTopo() == None or (pilha_ordenada.getTopo().getDado() >= self.getIni().getDado()):
                pilha_ordenada.insert(self.getIni().getDado())
            else:
                while pilha_ordenada.getTopo() != None and pilha_ordenada.getTopo().getDado() <= self.getIni().getDado():
                    pilha_auxiliar.insert(pilha_ordenada.getTopo().getDado())
                    pilha_ordenada.remove()
                pilha_ordenada.insert(self.getIni().getDado())
                while pilha_auxiliar.getSize() >= 0 and pilha_auxiliar.getTopo()!= None:
                    pilha_ordenada.insert(pilha_auxiliar.getTopo().getDado())
                    pilha_auxiliar.remove()
            self.remove()
        while pilha_ordenada.getTopo() != None:
            self.insert(pilha_ordenada.getTopo().getDado())
            pilha_ordenada.remove()