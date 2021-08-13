from fila_encadeada import*
from pilha_encadeada import*
from functions import*
import random

fila = Fila()
pilha1 = PilhaEncadeada()
pilha2 = PilhaEncadeada()

for i in range(14):
    fila.insert(random.randint(1,999))

print(fila)
fila.sort()
print(fila)