from Class import Carro
from Structs import Tabela


tabela = Tabela(1)
carro = Carro()
carro2 = Carro()
carro3 = Carro()

carro.setAno(1994)
carro.setDono('Anderson')
carro.setModelo('Golf')
carro.setPlaca('ABC123')

carro2.setAno(1995)
carro2.setDono('Ricado')
carro2.setModelo('Golf')
carro2.setPlaca('ABC124')

carro3.setAno(1996)
carro3.setDono('Fernando')
carro3.setModelo('Ford K')
carro3.setPlaca('DFG124')

tabela.insert(carro)
tabela.insert(carro2)
tabela.insert(carro3)

tabela._search(carro3)

print(tabela)