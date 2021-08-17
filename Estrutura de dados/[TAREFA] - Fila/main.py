from fila_encadeada import*
from pilha_encadeada import*
from functions import*

bar = '='*50
line = '-'*50
fila = Fila()

print(bar)
print('1 - Inserir um elemento na fila')
print('2 - Remover o elemento na fila')
print('3 - Destruir a fila')
print('4 - Ordenar a fila')
print(bar)
while True:
    print(line)
    oper = input('Digite a opção desejada: ')
    if oper == '1':
        print(line)
        elem = int(input('Digite o número desejado: '))
        fila.insert(elem)
        print('Sua fila atual')
        print(fila)
    if oper == '2':
        print(line)
        fila.remove()
        print('Elemento removido.')
        print(fila)
    if oper == '3':
        print(line)
        print('Deseja destruir a fila: [S]im [N]ão.')
        confirm = input(':')
        if confirm == 'S' or confirm == 's':
            fila.destroy()
    if oper == '4':
        print(line)
        fila.sort()
        print('Fila ordenada.')
        print(fila)
    else:
        print(line)
        print('Deseja finalizar o programa: [S]im [N]ão.')
        end = input(':')
        if end == 'S' or end == 's':
            break