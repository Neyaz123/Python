def summ(x, y, z):
    return x+y+z

def proizv(x, y, z):
    return x*y*z

X = int(input('Введите первое число: '))
Y = int(input('Введите второе число: '))
Z = float(input('Введите третье число: '))
print('Сумма введенных чисел: ', summ(X, Y, Z))
print('Произведение введенных чисел', proizv(X, Y, Z))
