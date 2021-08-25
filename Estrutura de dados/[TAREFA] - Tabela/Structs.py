class Tabela:
    def __init__(self,size):
        self._table = size
        self._key = [None] * (self._table + 1)
        self._value = [None] * (self._table + 1)
        self._size = 0
        self._ini = 1
    
    def __repr__(self):
        string = ''
        for i in range(self._ini, self._size + 1):
            string += str(self._value[i]) + '\n'
        return string

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self._size == self._table:
            return True
        else:
            return False

    def _search(self,value):
        if (not self.isEmpty()):
            for i in range(self._ini, self._size + 1):
                if self._key[i] == value.getPlaca():
                    return i
        return 0

    def look(self,value):
        index = self._search(value)
        if index > 0:
            return self._value[index]
    
    def _sort(self):
        pass

    def insert(self,value):
        index = self._search(value)
        if index > 0:
            self._value[index] = value
        elif (not self.isFull()):
            self._size += 1
            self._key[self._size] = value.getPlaca()
            self._value[self._size] = value
        
        self._sort
    
    def remove(self,value):
        index = self._search(value)
        if index > 0:
            for i in range(index, self._size + 1):           
                self._key[i] = self._key[i+1]
                self._value[i] = self._value[i+1]
            self._size -= 1
        else:
            return False