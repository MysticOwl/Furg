from _class import *
from product import *

lista = Lista(10)

lista.startLista(5,0)
lista.insert(5,1)
lista.insert(5,2)
lista.insert(5,3)
print(lista)
print(lista.vetor)
lista.remove(3)
print(lista)