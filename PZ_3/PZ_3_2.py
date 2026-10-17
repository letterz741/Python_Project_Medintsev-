#Даны два числа. Вывести вначале большее, а затем меньшее из них.
while True:
    try:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите числа")

if first >= second:
    print("Большее число:", first)
    print("Меньшее число:", second)
else:
    print("Большее число:", second)
    print("Меньшее число:", first)