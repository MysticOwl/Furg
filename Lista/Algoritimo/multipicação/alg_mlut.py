def Karatsuba(x, y):
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

    ac = Karatsuba(num1, num2)
    bd = Karatsuba(rem1, rem2)
    ad_plus_bc = Karatsuba(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

def diviConq(x,y):
    if (len(str(x))) == 1 and (len(str(y))) == 1:
        return x*y
    n = max(len(str(x)),len(str(y)))
    n2 = round(n/2)
    
    x0 = x // 10**n2
    x1 = x % 10**n2

    y0 = y // 10**n2
    y1 = y % 10**n2

    x_quad = diviConq(x0,x1)
    y_quad = diviConq(y0,y1)
    return (x0 * 10**n2 + x1) * (y0 * 10**n2 + y1)

def laRusse(x,y):
    imp=0

    if (x == 1):
        return y + imp

    elif (x%2==1):
        imp += y
        x = x - 1

    x = x // 2
    y = y * 2

    mult = laRusse(x,y)

    return mult + imp

x = 22343212
y = 67892121

#print(Karatsuba(x,y))
print(diviConq(x,y))
#print(laRusse(x,y))