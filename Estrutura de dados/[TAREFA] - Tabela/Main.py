from Class import Carro
from Structs import Tabela
import os , platform

so = platform.system()

bar = '='*50
line = '-'*50
table = int(input('Digite o tamanho da tabela: '))
tabela = Tabela(table)

while True:
    print('=======================Menu=======================')
    print('Toda a pesquisa sera feita a partir da placa!')
    print('1 - Inserir um item.')
    print('2 - Remover um item.')
    print('3 - Mostrar um item.')
    print('4 - Destuir a tabela.')
    print(bar)
    print('Tabela atual:\n')
    print(tabela)
    print(line)
    oper = str(input('Digite sua opção: '))
    if oper == '1':
        carro = Carro()
        print(line)
        carro.setPlaca(input('Digite a placa do carro: '))
        carro.setAno(input('Digite o ano do carro: '))
        carro.setDono(input('Digite o dono do carro: '))
        carro.setModelo(input('Digite o Modelo do carro: '))
        if (tabela.insert(carro)):
            print(line)
            print('Valor inserido.')
            print(line)
        else:
            print(line)
            print('Tabela cheia.')
            print(line)
    if oper == '2':
        print(line)
        if (tabela.remove(input('Digite a placa do carro que deseja remover: '))):
            print('Carro removido.')
        else:
            print('Placa não encontrada.')
    if oper == '3':
        print(line)
        placa = input('Digite a placa do carro: ')
        while True:
            metodo = input('Método de perquisa [B]inario [S]equencial: ')
            if (metodo == 'b' or metodo == 'B') or (metodo == 's' or metodo == 'S'):
                print(tabela.look(placa,metodo))
                break
            else:
                print('Comando invalido')
    if oper == '4':
        print(line)
        destroy = str(input('Destruir a tabela: [S]im [N]ão: '))
        if destroy == 's' or destroy == 'S':
            tabela.destroy()
            print('Tabela destruida.')
    print(line)
    out = input('Deseja encerrar o programa [S]im [N]ão:')
    if out == 's' or out == 'S':
        break
    if so == 'Windows':
        os.system('cls')
    else:
        os.system('clear')