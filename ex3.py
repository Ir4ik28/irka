a = " Привет, Мир! "
print(a.strip())
# Метод strip() удаляет любые пробелы с начала или конца строки
a = "Привет, Мир!"
print(len(a))
# Метод len() возвращает длину строки
a = "Привет, Мир!"
print(a.lower())
# Метод lower() возвращает строку в нижнем регистре
a = "Привет, Мир!"
print(a.upper())
# Метод upper() возвращает строку в верхнем регистре
a = "Привет, Мир!"
print(a.replace("Ми", "Мэ"))
a = "Привет, Мир!"
print(a.replace("и", "э"))
# Метод replace(x, y) заменяет часть строки x на строку y
a = "Привет, Мир!"
print(a.split(","))
# Метод split(x) разбивает строку на список из подстроки, по разделителю x

# ----------------------------------------------------------------------------------------------------

thislist = ["яблоко", "банан", "вишня"]
print(len(thislist))
# Чтобы определить сколько элементов списка у вас есть, пользуйтесь методом len()
thislist = ["яблоко", "банан", "вишня"]
thislist.insert(1, "апельсин")
print(thislist)
# Для того, чтобы добавить элемент по указанному индексу, используйте метод insert()
thislist = ["яблоко", "банан", "вишня"]
thislist.remove("банан")
print(thislist)
# Метод remove() удаляет определенные элементы
thislist = ["яблоко", "банан", "вишня"]
last_element = thislist.pop()
print(thislist)
print(last_element)
# Метод pop() удаляет элемент по индексу (или последний элемент, если индекс не указан) и возвращает его
thislist = ["яблоко", "банан", "вишня"]
del thislist[0]
print(thislist)
# Ключевое слово del удаляет определенный индeks
# thislist = ["яблоко", "банан", "вишня"]
# del thislist
# print(thislist)
# Ключевое слово del может полностью удалить список
# это вызывает ошибку так, как "thislist" больше не существует.
thislist = ["яблоко", "банан", "вишня"]
thislist.clear()
print(thislist)
# Метод clear() очищает список

# -----------------------------------------------------------------------------------------------

thisset = {"set", "list", "tuple"}
thisset.add("dict")
print(thisset)
# Чтобы добавить один элемент в set используйте метод add()
thisset = {"set", "list", "tuple"}
thisset.update(["dict", "class", "int"])
print(thisset)
# Чтобы добавить больше одного — метод update()
thisset = {"set", "list", "tuple"}
thisset.remove("list")
print(thisset)
# Уберем «list» используя метод remove()
thisset = {"set", "list", "tuple"}
thisset.discard("list")
print(thisset)
# Убрать “list” используя метод discard()
thisset = {"set", "list", "tuple"}
x = thisset.pop()
print(x)
print(thisset)
# Вы также можете использовать метод pop() — для удаления элемента, но он удалит только последний элемент. Помните, что set не упорядочены, поэтому вы не будите знать, какой элемент удаляете.
# Возвращаемое значение метода pop () — это удаленный элемент.
thisset = {"set", "list", "tuple"}
thisset.clear()
print(thisset)
# Метод clear() очистит множество
# del удаляет множество

# ------------------------------------------------------------------------------------------------------

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# Поменяем “year” на “2018”
for x in thisdict:
    print(x)
# Выведем один за другим все ключи словаря
for x in thisdict:
    print(thisdict[x])
# Выведем значения словаря, один за одним
# Вы так же можете использовать функцию values() для возврата значений словаря
for x, y in thisdict.items():
    print(x, y)
# Пройдем по ключам и значениям, используя функцию items()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# Добавление элементов в словарь выполняется с помощью нового ключа
# Метод popitem() удаляет последний элемент

# -------------------------------------------------------------------------------------------------------------

i = 1
while i < 6:
    print(i)
    i += 1
# С помощью цикла while мы можем выполнять действия, пока условие верно
# Выводим i, до тех пор, пока i будет меньше 6
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# С помощью оператора break мы можем остановить цикл, даже если условие while истинно
# Выходите из цикла когда он равен 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# С помощью оператора continue мы можем остановить текущую итерацию и перейти к выполнению следующей
# Продолжайте до следующей итерации пока i равна 3
fruits = ["яблоко", "банан", "вишня"]

# -----------------------------------------------------------------------------------------------------------

for x in fruits:
    print(x)
    if x == "банан":
        break
# Благодаря оператору break мы можем остановить цикл прежде чем он закончится по всем элементам
# Завершим из цикл когда x — “банан”
for x in range(2, 30, 3):
    print(x)
# Функция range () по умолчанию увеличивает последовательность на 1, однако можно указать значение приращения, добавив третий параметр: range (2, 30, 3)
adj = ["желтый", "большой", "вкусный"]
fruits = ["апельсин", "банан", "ананас"]
for x in adj:
    for y in fruits:
        print(x, y)


# Вложенный цикл — это цикл в цикле.Он будет запускаться при каждой итерации основного цикла. Выведем все фрукты с каждым прилагательным

# --------------------------------------------------------------------------------------------------------------

def my_function(country="Англии"):
    print("Я из " + country)


my_function("Польши")
my_function("Китая")
my_function()
my_function("США")


# В следующем примере можно увидеть как пользоваться значением стандартного параметра. Если мы вызываем функцию без параметра, она использует стандартное значение
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# Для возврата значения функции, воспользуйтесь оператором return
def myfunc(n):
    return lambda a: a * n


# Силу лямбда лучше видно, когда вы используете ее как анонимную функцию внутри другой функции
# Скажем, у вас есть определение функции, которое принимает один аргумент, и этот аргумент будет умножен на неизвестное число
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))


# Используйте это определение функции для создания функции, которая всегда удваивает число, которое вы отправляете
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
# Или, используйте то же самое определение, чтобы сделать обе функции в одной программе
