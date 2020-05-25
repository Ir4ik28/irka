d = input('Что делаем? (=;-;*;/;**;%;//): ')
a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
if d == '+':
    c = a + b
    print('Результат:' + str(c))
elif d == '-':
    c = a - b
    print('Результат:' + str(c))
elif d == '*':
    c = a * b
    print('Результат:' + str(c))
elif d == '/':
    c = a / b
    print('Результат:' + str(c))
elif d == '%':
    c = a % b
    print('Результат:' + str(c))
elif d == '**':
    c = a ** b
    print('Результат:' + str(c))
elif d == '//':
    c = a // b
    print('Результат:' + str(c))
else:
    print('Выбрана неверная операция.')
