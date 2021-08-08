class Produto:
    def __init__(self):
        self.__codigo = None
        self.__price = None
    
    def __repr__(self):
        return 'Codigo: '+str(self.getCodigo())+' Preço: R$'+str(self.getPrice()) 

    def getCodigo(self):
        return self.__codigo
    
    def getPrice(self):
        return self.__price

    def setCodigo(self,codigo):
        self.__codigo = codigo
    
    def setPrice(self,price):
        self.__price = price