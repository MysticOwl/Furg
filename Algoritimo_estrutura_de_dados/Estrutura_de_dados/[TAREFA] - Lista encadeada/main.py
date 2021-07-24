from classes import *

lista = Lista()
print('-------------------------------------------------------------------------------------')
print('Lista atual                      :', lista)
print('Primeiro elemento da lista       :', lista.getHead())
print('Tamanho atual da lista           :', lista.getSize())
print('-------------------------------------------------------------------------------------')

node1 = lista.first("1")

print('-------------------------------------------------------------------------------------')
print('Lista atual                      :', lista)
print('Primeiro elemento da lista       :', lista.getHead())
print('Tamanho atual da lista           :', lista.getSize())
print('-------------------------------------------------------------------------------------')

node2 = lista.addList("2")

print('-------------------------------------------------------------------------------------')
print('Lista atual                      :', lista)
print('Primeiro elemento da lista       :', lista.getHead())
print('Tamanho atual da lista           :', lista.getSize())
print('-------------------------------------------------------------------------------------')