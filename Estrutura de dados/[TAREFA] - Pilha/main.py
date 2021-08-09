from os import remove
from typing import Sized
from pilha_encadeada import *
from pilha_contiguidade import *
from modulo import comparaPilhas
from product import *

# Check list:
#     Instanciar Classes                  :
#     Menu de inserir e remover           :
#     Destruir pilhas                     :
#     Comprar pilhas                      :

bar = '=' *50
line = '-' * 50
pilha_enca = PilhaEncadeada()
size = int(input('Digite o tamanho da lista por contiguidade: '))
pilha_cont = PilhaContiguidade(size)

print(bar)
print('1 - Inserir um elemento na pilha')
print('2 - Remover um elemento na pilha ')
print('3 - Consultar o topo da pilha')
print('4 - Destruir a pilha')
print('5 - Compara as duas pilhas')
print('6 - Mostrar as pilhas')
print(bar)
while True:
    print(line)
    oper = input('Digite a operação desejada: ')
    print(line)
    if oper == '1':
        elem = input('Digite o elemento que deseja inserir: ')
        print(line)
        inser_pilha = input('Qual pilha deseja inserir: [E]ncadeada ou [C]ontigua: ')
        if inser_pilha == 'E' or inser_pilha == 'e':
            pilha_enca.insert(elem)
        if inser_pilha == 'C' or inser_pilha == 'c':
            pilha_cont.insert(elem)
    if oper == '2':
        print(line)
        remove_pilha = ('Qual pilha deseja remover: [E]ncadeada ou [C]ontigua: ')
        if remove_pilha == 'E' or remove_pilha == 'e':
            pilha_enca.remove()
        if remove_pilha == 'C' or remove_pilha == 'c':
            pilha_cont.remove()
    if oper == '3':
        print(line)
        cons_pilha = input('Qual pilha deseja consultar: [E]ncadeada ou [C]ontigua: ')
        if cons_pilha == 'E' or cons_pilha == 'e':
            print(line)
            print(pilha_enca.topoPilha())
        if cons_pilha == 'C' or cons_pilha == 'c':
            print(line)
            print(pilha_cont.getTopo())
    if oper == '4':
        destroy_pilha = input('Qual pilha deseja destruir: [E]ncadeada ou [C]ontigua: ')
        if destroy_pilha == 'E' or destroy_pilha == 'e':
            pilha_enca.destroy()
        if destroy_pilha == 'C' or destroy_pilha == 'c':
            pilha_cont.destroy()
    if oper == '5':
        if (comparaPilhas(pilha_enca,pilha_cont)):
            print('As pilhas são iguais')
        else:
            print('As pilhas são diferentes')
    if oper == '6':
        print(line)
        print('Pilha encadeada:',pilha_enca)
        print(line)
        print('Pilha contigua:',pilha_cont)
    print(line)
    stop = input('Deseja continuar: [S]im [N]ão: ')
    if stop == 'N' or stop == 'n':
        break