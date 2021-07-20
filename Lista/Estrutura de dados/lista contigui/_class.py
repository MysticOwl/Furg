class Lista:
    def __init__(self,size):
        self.size = size
        self.vetor = [None] *size
        self.iniArea = -1
        self.fimArea = -1

    def __repr__(self):
        string = "Inicio-"
        for i in range(self.iniArea-1, self.fimArea):
            string += str((self.vetor[i])) + "-"
        return string + ">Fim"

    def vazia(self):
        if self.iniArea == -1 and self.fimArea == -1:
            return True
        else:
            return False

    def sizeLista(self):
        if self.fimArea == -1 and self.iniArea == -1:
            return 0
        elif self.iniArea == self.fimArea:
            return 1
        else:
            return (self.fimArea + 1) - self.iniArea
    
    def getSize(self):
        return self.size        

    def getSizeLogico(self):
        return self.getSize() - 1

    def startLista(self,index,elem):
        if index == 0 or index == self.getSize() +1:
            raise IndexError("Indice fora de posição.")
        index -=1
        if (self.iniArea >= 0) or (self.fimArea <= self.getSizeLogico()):
            if (self.vazia()):
                self.iniArea = 0
                self.fimArea = 0
                for i in range(self.iniArea, self.getSize()):
                    if i == index:
                        self.vetor[i] = elem
                        self.iniArea = index + 1
                        self.fimArea = index + 1
        else:
            return False

    def insert(self,index,elem):
        if(self.insertIni(index,elem)):
            return True
        elif(self.insertFim(index,elem)):
            return True
        else:
            index -= 1
            if(self.iniArea == 0 or ((self.getSize() < self.fimArea))) and (index>(self.getSize()//2)):
                for i in range(self.iniArea - 1,self.iniArea):
                    self.vetor[i-1] = self.vetor[i]
                    self.vetor[i] = elem
                self.iniArea = self.iniArea - 1
            else:
                for i in range(self.fimArea,self.fimArea + 1):
                    self.vetor[i+1] = self.vetor[i]
                    self.vetor[i] = elem
                self.fimArea = self.fimArea + 1
    
    def insertIni(self,index,elem):
        if((index <= self.iniArea) and self.iniArea > 0):
            index -= 1
            for i in range(self.iniArea - 1,self.iniArea):
                self.vetor[i-1] = self.vetor[i]
                self.vetor[i] = elem
            self.iniArea = self.iniArea - 1
            return True
        else:
            return False
    
    def insertFim(self,index,elem):
        if((index >= self.fimArea) and self.fimArea < self.getSize()):
            for i in range(self.fimArea,self.fimArea + 1):
                self.vetor[i+1] = self.vetor[i]
                self.vetor[i] = elem
            self.fimArea = self.fimArea + 1
            return True
        else:
            return False
                
    def clear(self):
        self.vetor = [None] *self.size
        self.iniArea = -1
        self.fimArea = -1