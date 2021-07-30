def mult(x,y):
    if (x < 10 ):
        return (x * y)
    n = (len(str(x))-1)
    soma = ((x//10**n) * y)*10**n
    x = x%10**n

    return soma + mult(x,y)

def soma(x,y):
    if x > y:
        while y > 0:
            x += 1
            y -= 1
        return x
    else:
        while x > 0:
            y += 1
            x -= 1
        return y