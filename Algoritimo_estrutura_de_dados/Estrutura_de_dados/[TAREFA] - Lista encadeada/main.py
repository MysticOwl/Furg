from classes import *
import random


bar = '='*90
print(bar)
print('Lista iniciada')
lista = Lista()
for i in range(10):
    lista.addInList(i,str(random.randint(1,999)))
print(lista)
print(bar)
print('1 - Inserir um elemento na posição:')
print('2 - Remover da posição:')
print('3 - Revelar o valor da posição:')
print('4 - Revelar a posição do valor:')
print('5 - Destruir a lista:')
print(bar)
while True:    
    oper = input('Digite a operação desejada: ')  
    if int(oper) == 1:
        elem = input('Digite o elemento que deseja inserir: ')        
        print(bar)
        if lista.isEmpty():
            print("Lista vazia. Posição 1 é a única disponível.")
            lista.addInList(1,elem)
        else:
            index = int(input('Digite a posição desejada.\nPosições aceitas de 1 até {}: '.format(lista.getSize()+1)))
            if (1 < index > (lista.getSize()+1)):
                print('ERROR! Posição invalida')
            else:
                lista.addInList(index,elem)
        print(bar)        
    elif int(oper) == 2:
        print(bar)
        if lista.isEmpty():
            print("Operação bloqueada, a lista se encontra vazia no momento.")
        else:
            index = int(input('Digite a posição desejada.\nPosições aceitas de 1 até {}: '.format(lista.getSize()+1)))
            if 1 < index > (lista.getSize()+1):
                print('ERROR! Posição invalida')
            else:
                lista.removeIn(index)
                print('O elemento foi removido com sucesso.')
        print(bar)
    elif int(oper) == 3:
        print(bar)
        index = int(input('A posição para saber o elemento: '))
        print(bar)
        if (lista.getItem(index)):
            print('A posição {} contem o elemento {}:'.format(index,lista.getItem(index)))
        else:
            print('ERROR!, posição invalida')
        print(bar)
    elif int(oper) == 4:
        print(bar)
        elem = input('Digite o elemento para saber sua posição: ')
        print(bar)
        if (lista.search(elem)):
            print(lista.search(elem))
        else:
            print('ERROR! Elemento não se encontra na lista')
        print(bar)
    elif int(oper) == 5:
        print(bar)
        oper = input('Deseja realmente destruir a lista?\n [S]im - [N]ão: ')
        print(bar)
        if oper == 'S':
            lista.destroy()
    else:
        print(bar)
        oper = input('Deseja sair?\n [S]im - [N]ão: ')
        print(bar)
        if oper == 'S':
            False
    print('Lista Atualizada:\n',lista)