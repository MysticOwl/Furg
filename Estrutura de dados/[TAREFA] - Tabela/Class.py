class Carro:
    def __init__(self):
        self.__placa = None
        self.__ano = None
        self.__dono = None
        self.__modelo = None
    
    def __repr__(self):
        return 'Placa:' + str(self.getPlaca()) + ' Ano:' + str(self.getAno()) + ' Dono:' + str(self.getDono()) + ' Modelo:' + str(self.getModelo())

    def getPlaca(self):
        return self.__placa
    
    def getAno(self):
        return self.__ano
    
    def getDono(self):
        return self.__dono

    def getModelo(self):
        return self.__modelo
    
    def setPlaca(self, value):
        self.__placa = str(value)
    
    def setAno(self, value):
        self.__ano = str(value)
    
    def setDono(self, value):
        self.__dono = str(value)
    
    def setModelo(self, value):
        self.__modelo = str(value)