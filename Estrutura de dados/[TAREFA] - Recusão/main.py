
# Todos os exercícios se encontram nas respectivas funções
# Para testar os algoritimos basta chamar a função e o valor que deseja

# =============== Exercícios 1 =============== #

def soma_recusao(vet):
    if len(vet) == 1:
        return vet[0]
    aux = len(vet) - 1
    soma_vector = vet[aux]    
    vet.pop()
    last_index = soma_recusao(vet) + soma_vector
    return last_index

# =============== Exercícios 2 =============== #

def fatorial(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * fatorial(num - 1)

# =============== Exercícios 3 =============== #

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

# =============== Exercícios 4 =============== #

def soma_digito(num):
    if len(str(num)) == 1:
        return num    
    ultimo_digito = num % 10
    num = num // 10
    return soma_digito(num) + ultimo_digito