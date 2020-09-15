def sredn(a=10, b=6, c=20):
    return ((a+b+c)/3)
print (sredn())
x1, x2, x3 = map(int,input('Введите три числа через пробел:').split())
arifm = sredn(x1, x2, x3)
print (arifm)
