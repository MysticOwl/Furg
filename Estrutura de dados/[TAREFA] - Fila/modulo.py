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