number = int(input("Enter a number you want to convert: "))
metric = input("Enter km or ml: ")

def convert(val1, val2):
    if val2 == "km":
        result = val1 * 1.6
    elif val2 == "ml":
        result = val1 / 1.6
    else:
        print("Bad input")
    print(result)
    return result

convert(number, metric)
number = int(input("Enter a number you want to convert: "))
metric = input("Enter km or ml: ")

def convert(val1, val2):
    if val2 == "km":
        result = val1 * 1.6
    elif val2 == "ml":
        result = val1 / 1.6
    else:
        print("Bad input")
    print(result)
    return result

convert(number, metric)