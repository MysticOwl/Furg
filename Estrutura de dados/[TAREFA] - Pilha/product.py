class Produto:
    def __init__(self):
        self.__codigo = None
        self.__price = None
    
    def getCodigo(self):
        return self.__codigo
    
    def getPrice(self):
        return self.__price

    def setCodigo(self,codigo):
        self.__codigo = codigo
    
    def setPrice(self,price):
        self.__price = price