bicycles = ['trek', 'cannondale', 'redline', 'special']
print(bicycles[0])


bicycles = ['trek', 'cannondale', 'redline', 'special']
print(bicycles[0].title())


bicycles = ['trek', 'cannondale', 'redline', 'special']
message = f"Мой первый велосипед был {bicycles[0].title()}."
print(message)


friends = ['Artem', 'Nastya', 'Marina', 'Masha', 'Viktor']
print(friends[1])
print(friends[-1])
sms = f'Мой лучший друг - {friends[4]}'
sms1 = f'Мой лучший друг - {friends[0]}'
sms2 = f'Мой лучший друг - {friends[3]}'
sms3 = f'Мой лучший друг - {friends[1]}'
sms4 = f'Мой лучший друг - {friends[2]}'
print(sms)
print(sms1)
print(sms2)
print(sms3)
print(sms4)


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert (0, 'ducati')
print(motorcycles)

мотоциклы = ['honda', 'yamaha', 'suzuki']
del  мотоциклы[0]
print(мотоциклы)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop ()
print (f"Последний принадлежавший мне мотоцикл был {last_owned.title ()}.")
# Если вы не уверены, использовать ли оператор del или метод pop () , вот простой способ решить:
# когда вы хотите удалить элемент из списка и никоим образом не использовать этот элемент, используйте оператор del ; если вы хотите использовать элемент при его удалении, используйте метод pop () .


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort ()
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort (reverse = True)
print (cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

