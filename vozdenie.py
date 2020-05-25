def car_18(x, y):
    if y > 18:
        print(f'{x} может водить машину')
    elif y < 18:
        print(f'{x} не может водить машину')
    else:
        print('команда введена не верно')
    return


car_18('Ринат', 28)
