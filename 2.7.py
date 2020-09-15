def days(k):
    return k%7 + 1
try:
    K = int(input('Введите номер дня этого года от 1 до 365 включительно: '))
    if K > 365 or K < 1:
        raise ValueError()
    else: print('Номер дня недели(1 - понедельник, 7 - воскресенье): ', days(K))
except ValueError:
    print('Неверно введено число!')
    

