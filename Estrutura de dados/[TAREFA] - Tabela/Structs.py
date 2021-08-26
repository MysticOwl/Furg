class Tabela:
    def __init__(self,size):
        self._table = size
        self._key = [None] * (self._table + 1)
        self._value = [None] * (self._table + 1)
        self._size = 0
        self._ini = 1
    
    def __repr__(self):
        string = ''
        if self._size == 0:
            return 'Tabela Vazia'
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

    def _linearSearch(self,value):
        if (not self.isEmpty()):
            for i in range(self._ini, self._size + 1):
                if self._key[i] == value:
                    return i
        return 0
    
    def _binarySearch(self,value):
        if (not self.isEmpty()):
            self._sort
            aux_ini = self._ini
            aux_fim = self._size
            while aux_ini <= aux_fim:
                middle = (aux_ini + aux_fim)//2
                if str(self._key[middle]) == value:
                    return self._value[middle]
                else:
                    if str(self._key[middle]) < value:
                        aux_fim = middle - 1
                    else:
                        aux_ini = middle + 1
            return 0

    def look(self,value, param):
        if param == 'l' or param == 'L':
            index = self._linearSearch(value)
            if index > 0:
                return self._value[index]
        elif param == 'b' or param == 'B':
            self._binarySearch(value)
        else:
            return False
    
    def _sort(self):
        aux_key = ''
        aux_value = ''
        for i in range(self._ini, self._size + 1):
            for j in range(self._ini , self._size + 1):
                if self._key[i] < self._key[j]:
                    aux_key = self._key[i]
                    self._key[i] = self._key[j]
                    self._key[j] = aux_key
                    aux_value = self._value[i]
                    self._value[i] = self._value[j]
                    self._value[j] = aux_value                    

    def insert(self,value):
        index = self._linearSearch(value)
        if index > 0:
            self._value[index] = value
        elif (not self.isFull()):
            self._size += 1
            self._key[self._size] = value.getPlaca()
            self._value[self._size] = value
    
    def remove(self,value):
        index = self._linearSearch(value)
        if index > 0:
            for i in range(index, self._size + 1):           
                self._key[i] = self._key[i+1]
                self._value[i] = self._value[i+1]
            self._size -= 1
        else:
            return False
    
    def destroy(self):
        self._size = 0