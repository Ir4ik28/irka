import pyinputplus as pyip

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    elif age > 150:
        print('Please enter real number.')
        continue
    break
print(f'Your age is {age}.')
# -------------------------------------------------------------
import pyinputplus as pyip

response = pyip.inputNum('Enter a number: ')
print(response)
# -------------------------------------------------------------
response = pyip.inputInt(prompt='Enter a number: ')
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', min=4)
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', greaterThan=4)
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num 4<x<6: ', min=4, lessThan=6)
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ')
print(response)
response = pyip.inputNum('Enter num: ', blank=True)
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', limit=2, timeout=10)
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', limit=2, default='N/A')
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', allowRegexes=[r'(I|V|X|L|C|D|M|i|v|x|l|c|d|m)+', r'zero'])
print(response)
# -------------------------------------------------------------
response = pyip.inputNum('Enter num: ', blockRegexes=[r'[02468]$'])
print(response)
# -------------------------------------------------------------
response = pyip.inputStr('Enter num: ', allowRegexes=[r'caterpillar', 'cate-gory'], blockRegexes=[r'cat'])
print(response)


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must addupto10,not%s.' % (sum(numbersList)))
    return int(numbers)


response = pyip.inputCustom(addsUpToTen)
print(response)
# функция мега сложная и непонятная
