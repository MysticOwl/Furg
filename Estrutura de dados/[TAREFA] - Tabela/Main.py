from Class import Carro
from Structs import Tabela


tabela = Tabela(4)
carro = Carro()
carro2 = Carro()
carro3 = Carro()

carro.setAno(1994)
carro.setDono('Anderson')
carro.setModelo('Golf')
carro.setPlaca('ABC124')

carro2.setAno(1995)
carro2.setDono('Ricado')
carro2.setModelo('Golf')
carro2.setPlaca('DFG124')

carro3.setAno(1996)
carro3.setDono('Fernando')
carro3.setModelo('Ford K')
carro3.setPlaca('ABC123')

tabela.insert(carro)
tabela.insert(carro2)
tabela.insert(carro3)

print(tabela._binarySearch('ABC123'))