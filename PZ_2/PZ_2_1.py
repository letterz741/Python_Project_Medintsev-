number = int(input("Введите трехзначное число: "))

a = number // 100
b = number // 10 % 10
c = number % 10

print(b * 100 + a * 10 + c)
