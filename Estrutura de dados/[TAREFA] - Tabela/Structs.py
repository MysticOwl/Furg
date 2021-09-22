class Tabela:
    def __init__(self,size):
        '''
        Método construtor da tabela
        '''
        self._table = size
        self._key = [None] * (self._table + 1)
        self._value = [None] * (self._table + 1)
        self._size = 0
        self._ini = 1
    
    def __repr__(self):
        '''
        Representação da tabela
        '''
        string = ''
        if self._size == 0:
            return 'Vazia'
        for i in range(self._ini, self._size + 1):
            string += str(self._value[i]) + '\n'
        return string

    def isEmpty(self):
        '''
        Método verificador para saber se a tabela é vazia
        '''
        if self._size == 0:
            return True
        else:
            return False
    
    def isFull(self):
        '''
        Método verificador para saber se a tabela está cheia
        '''
        if self._size == self._table:
            return True
        else:
            return False

    def _sequentialSearch(self,value):
        '''
        Método de busca sequencial
        '''        
        if (not self.isEmpty()):
            for i in range(self._ini, self._size + 1):
                if self._key[i] == value:
                    return i
        return 0
    
    def _binary_recursion(self,ini,fim,value):
        mid = (ini+fim)//2
        if str(self._key[mid]) == value:
            return mid
        if str(self._key[mid]) < value:
            fim = mid - 1
        else:
            print('else')
            ini = mid + 1
        recursion = self._binary_recursion(ini,fim,value)
        return recursion

    def _binarySearch(self,value):
        '''
        Método de busca binária
        '''
        if (not self.isEmpty()):
            self._sort
            return self._binary_recursion(self._ini,self._size,value)              
        return 0

    def look(self,value, param):
        '''
        Método responsável por mostrar o valor inteiro
        Recebendo como parâmetro o método de busca
        '''
        if param == 's' or param == 'S':
            index = self._sequentialSearch(value)
            if index > 0:
                return self._value[index]
            else:
                return False
        elif param == 'b' or param == 'B':
            index = self._binarySearch(value)
            if index > 0:
                return self._value[index]
            else:
                return False
        else:
            return False
    
    def _sort(self):
        '''
        Método para organizar a tabela sequencialmente
        '''
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
        '''
        Método que insere um objeto no final da tabela
        '''
        index = self._sequentialSearch(value)
        if index > 0:
            self._value[index] = value
            return True
        elif (not self.isFull()):
            self._size += 1
            self._key[self._size] = value.getPlaca()
            self._value[self._size] = value
            return True
        return False
    
    def remove(self,value):
        '''
        Método para remoção de uma determinada chave
        '''
        index = self._binarySearch(value)
        if index > 0:
            for i in range(index, self._size + 1):           
                self._key[i] = self._key[i+1]
                self._value[i] = self._value[i+1]
            self._size -= 1
            return True
        else:
            return False
    
    def destroy(self):
        self._size = 0