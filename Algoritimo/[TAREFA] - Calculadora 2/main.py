import timeit
def soma(oper1,oper2):
    string_oper1 = str(oper1)
    string_oper2 = str(oper2)

    aux_div = 0
    aux_soma = 0
    cont = 0

    resultado = []

    for i in range(max(len(string_oper1),len(string_oper2)),0,-1):
        aux_soma = int(string_oper1[i-1]) + int(string_oper1[i-1]) + aux_div
        resultado.insert(cont,aux_soma%10)
        cont += 1
        aux_div = aux_soma//10
    resultado.append(aux_div)
    resultado.reverse()
    return resultado

def mult(oper1,oper2):
    return

x = 9999999999
y = 9999999999

table = open('Resultado.txt','w',encoding='utf8')
bar = '=' *50
print('Favor esperar até que a janela se feche.')
print('Executando.....')
table.write('\n////=================MULTIPLICAÇÃO=================/////\n')
table.write('\n')
#loop de multiplicação
for i in range(1,11):
    ini_mult = timeit.default_timer()
    mult((x),(y))
    end_mult = timeit.default_timer()
    table.writelines([str(bar),'\n','Algoritmo de multiplicação\n','\nExecução                :',str(i),'\nTamanho de n            :',str(len(str(x))),'\nTempo de execução       :', str(end_mult-ini_mult),'\n'])
    x *= 10**(i*4000)
    y *= 10**(i*4000)

table.write('\n////=====================SOMA=====================/////\n')
table.write('\n')
print('Executando.....')
x = 9876543210
y = 1234567890
#loop de soma
for i in range(1,11):
    ini_soma = timeit.default_timer()
    soma((x),(y))
    end_soma = timeit.default_timer()
    table.writelines([str(bar),'\n','Algoritmo de soma\n','\nExecução                :',str(i),'\nTamanho de n            :',str(len(str(x))),'\nTempo de execução       :', str(end_soma-ini_soma),'\n'])
    x *= 10**(i*4000)
    y *= 10**(i*4000)    
table.close()