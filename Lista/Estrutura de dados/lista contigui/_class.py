class Lista:
    def __init__(self, size):
        self.size = size
        self.vector = [None] * self.size
        self.ini = -1
        self.end = -1

    def __repr__(self):
        string = "[ "
        for i in range(self.size):
            string = string + str(self.vector[i]) + ','
        return string + " ]"
    
    def vazia(self):
        if self.ini == -1 and self.end == -1:
            return True

    def len(self):
        if self.vazia():
            return 0
        else:
            return self.size

    def insert(self, index, elem):
        if index == 0:
            index = 1
        if self.vazia():
            self.ini = 0
            self.fim = 0
        elif (self.end != self.size -1):
            for i in range(self.end, self.ini + index -2, -1):    
                self.vector[i+1] = self.vector[i]
            self.fim = self.fim + 1
        else:
            for i in range(self.ini, self.ini, + index):
                self.vector[i-1] = self.vector[i]
            self.ini = self.ini - 1
        self.vector[self.ini + index - 1] = elem
        return self.vector
    
    def remove(self,index):
        if index == 0:
            index = 1
        if (index < 0) or (index > self.size):
            print(self.ini,self.end)
            raise IndexError('Indice fora da lista')
        else:
            for i in range(self.size):
                self.vector[i] = None
            return self.vector
    
    def location(self,elem):
        for i in range(self.size):
            if self.vector[i] == elem:
                if i == 0:
                    i = 1
                return ("Elemento {} no indice {}.".format(elem,i))
        return ValueError("O elemento {} não se encontra no vetor".format(elem))
    
    def clear(self):
        for i in range(self.size):
            self.vector[i] = None
        return self.vector