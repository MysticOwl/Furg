class Product:
    def __init__(self):
        self.code = None
        self.price = None

    def __repr__(self) :
        return "Codigo: " + str(self.code) + ". Preço: " + str(self.price)
    
    def getPrice(self):
        return self.price
    
    def getCode(self):
        return self.code
    
    def setPrice(self,value):
        self.price = value
    
    def setCode(self,value):
        self.code = value
