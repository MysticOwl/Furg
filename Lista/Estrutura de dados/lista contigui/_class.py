class Lista:
    def __init__(self, size):
        self.size = size
        self.vector = [None] * self.size
        self.ini = -1
        self.end = -1

    def __repr__(self):
        string = "[ "
        for i in range(self.ini , self.end + 1):
            string = string + ',' + str(self.vector[i])
        return string + " ]"
    
    def vazia(self):
        return self.ini == -1 or self.end == -1

    def len(self):
        if self.vazia():
            return 0
        else:
            return self.ini - self.end +1

    def insert(self, index, elem):
        for i in range(self.size):
            if i == index:
                self.vector[i -1] = elem
        else:
            raise IndexError("Indice fora da lista.")