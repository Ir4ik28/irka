VALID_COLORS = ['blue', 'red', 'black']


def get_color():
    while True:
        a = input('Напиши цвет ')
        if a in VALID_COLORS:
            print(a.upper())
            break
        elif a == 'выход':
            print('пока')
            break
        elif a not in VALID_COLORS:
            c = input('неверный цвет, хотите добавить цвет? ')
            if c == 'да':
                VALID_COLORS.append(a)
            elif c == 'нет':
                break

    return


get_color()
