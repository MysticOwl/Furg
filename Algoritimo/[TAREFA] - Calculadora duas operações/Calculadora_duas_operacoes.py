import timeit
def mult(x, y):
    
    if x < 10 and y < 10:
        return x * y
        
    num1_len = len(str(x))
    num2_len = len(str(y))

    n = max(num1_len,num2_len)
    
    nby2 = round(n/2)

    num1 = x // (10 ** nby2)
    rem1 = x % (10 ** nby2)

    num2 = y // (10 ** nby2)
    rem2 = y % (10 ** nby2)

    ac = mult(num1, num2)
    bd = mult(rem1, rem2)
    ad_plus_bc = mult(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

def soma(x,y):
    
    if (len(str(x))) == 1 and (len(str(y))) == 1:
        return x+y

    n = max(len(str(x)),len(str(y)))
    n2 = round(n/2)
    
    x0 = x // 10**n2
    x1 = x % 10**n2

    y0 = y // 10**n2
    y1 = y % 10**n2

    x = soma(x0,x1)
    y = soma(y0,y1)

    return (x0 * 10**n2 + x1) + (y0 * 10**n2 + y1)

x = 9876543210
y = 1234567890

table = open('Resultado.txt','w',encoding='utf8')
bar = '=' *50
print('Favor esperar até que a janela se feche.')
print('Executando.....')
table.write('\n////=================MULTIPLICAÇÃO=================/////\n')
table.write('\n')
#loop de multiplicação
for i in range(1,11):
    ini = timeit.default_timer()
    mult((x),(y))
    end = timeit.default_timer()
    table.writelines([str(bar),'\n','Algoritmo de multiplicação\n','\nExecução                :',str(i),'\nTamanho de n            :',str(len(str(x))),'\nTempo de execução       :', str(end-ini),'\n'])
    x *= 10**(i*4000)
    y *= 10**(i*4000)

table.write('\n////=====================SOMA=====================/////\n')
table.write('\n')
print('Executando.....')
x = 9876543210
y = 1234567890
#loop de soma
for i in range(1,11):
    ini = timeit.default_timer()
    soma((x),(y))
    end = timeit.default_timer()
    table.writelines([str(bar),'\n','Algoritmo de soma\n','\nExecução                :',str(i),'\nTamanho de n            :',str(len(str(x))),'\nTempo de execução       :', str(end-ini),'\n'])
    x *= 10**(i*4000)
    y *= 10**(i*4000)    
table.close()