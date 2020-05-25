d = input('что делаем? (мили в км или км в мили) :  ')
if d == 'мили в км':
    ml = float(input('введи число: '))
    c = ml * 1.6
    print(str(ml) + ' миль' + ' равняется ' + str(c) + str(' км'))
elif d == 'км в мили':
    km = float(input('введи число: '))
    a = km / 1.6
    print(str(km) + ' км' + ' равняется ' + str(a) + str(' миль'))
else:
    print('выбрана неверная операция')
