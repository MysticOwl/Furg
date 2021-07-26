from classes import *
oper = None
bar = '='*90
print(bar)
print('Lista iniciada')
lista = Lista()
print(bar)
print('1 - Inserir um elemento na posição:')
print('2 - Remover da posição:')
print('3 - Revelar o valor da posição:')
print('4 - Revelar a posição do valor:')
print('5 - Destruir a lista:')
print('6 - Quantidade de elementos:')
print('7 - Adicionar uma segunda lista encadeada:')
print('8 - Inverter a desejada:')
print('9 - Mostrar Lista')
print('0 - Para encerrar o programa:')
print(bar)
while oper != 'S':
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
                print(bar)
            else:
                lista.addInList(index,elem)      
    elif int(oper) == 2:
        print(bar)
        if lista.isEmpty():
            print(bar)
            print("A lista está vazia.")
            print(bar)
        else:
            index = int(input('Digite a posição desejada.\nPosições aceitas de 1 até {}: '.format(lista.getSize()+1)))
            if 1 < index > (lista.getSize()):
                print('ERROR! Posição invalida')
                print(bar)
            else:
                lista.removeIn(index)
                print('O elemento foi removido com sucesso.')
                print(bar)
    elif int(oper) == 3:
        if lista.isEmpty():
            print(bar)
            print('A lista está vazia.')
            print(bar)
        else:
            print(bar)
            index = int(input('Digite a de 1 até {} para saber o elemento: '))
            print(bar)
            if (lista.getItem(index)):
                print('A posição {} contem o elemento {}:'.format(index,lista.getItem(index)))
                print(bar)
            else:
                print('ERROR!, posição invalida')
                print(bar)
    elif int(oper) == 4:
        if lista.isEmpty():
            print(bar)
            print('A lista está vazia.')
            print(bar)
        else:
            print(bar)
            elem = input('Digite o elemento para saber sua posição: ')
            print(bar)
            if (lista.search(elem)):
                print(lista.search(elem))
                print(bar)
            else:
                print('ERROR! Elemento não se encontra na lista')
                print(bar)
    elif int(oper) == 5:
        print(bar)
        destroy = input('Deseja realmente destruir a lista?\n [S]im - [N]ão: ')
        print(bar)
        if destroy == 'S':
            lista.destroy()
    elif int(oper) == 6:
        print(bar)
        if lista.quantElem():
            print('Lista está atualmente vazia.')
            print(bar)
        else:
            print('A lista contem um total de {} elementos'.format(lista.quantElem()))
            print(bar)
    elif int(oper) == 7:
        secondList = Lista()
        print(bar)
        print('1 - Inserir (N) elemento:')
        print('2 - Comparar as Duas listas existentes:')
        print(bar)
        auxOper = input('Digite a operação desejada: ')
        print(bar)
        if int(auxOper) == 1:
            quant = int(input('Digite a quantidade de elementos: '))
            for i in range(1,quant+1):
                elem = input('Digite o elemento: ')
                secondList.addInList(i,elem)
            print(bar)
            print('Primeira lista:\n',lista,'\nSegunda lista:\n',secondList)
        elif int(auxOper) == 2:
            if (lista.equalList(secondList) == True):
                print('As listas são iguais!')
                print(bar)
            else:
                print('As listas são diferentes!')
                print(bar)
        else:
            print(bar)
            print('Listas de tamanhos diferentes:')
            print(bar)
    elif int(oper) == 8:
        if lista.isEmpty():
            print(bar)
            print('A lista está vazia.')
            print(bar)
        else:
            print(bar)
            print('Lista atual:\n', lista)
            print(bar)
            invert = input('Inverter lista [S]im - [N]ão: ')
            if invert == 'S':
                lista.reversList()
                print('Lista Invertida:\n',lista)
                print(bar)
    elif int(oper) == 9:
        print(bar)
        print('Lista:\n',lista)
        print(bar)
    else:
        print(bar)
        oper = input('Deseja sair?\n [S]im - [N]ão: ')
        print(bar)