def mult(x,y):
    if (x < 10 ):
        return (x * y)
    n = (len(str(x))-1)
    soma = ((x//10**n) * y)*10**n
    x = x%10**n

    return soma + mult(x,y)

def soma(x,y):
    if x > y:
        if y == 0:
            return x + y
        x += 1
        y -= 1
        return soma(x,y)
    else:
        if x == 0:
            return y + x
        x -= 1
        y += 1
        return soma(x,y)