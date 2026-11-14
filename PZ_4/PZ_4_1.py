#Дано вещественное число X и целое число N (> 0). Найти значение выражения
# 1 - X^2 (2!) + x^4/ (4! ) - ... + (-1)^N * X^(2*N) / ((2*N)!) (N! = 1*2...*N).
#Полученное число является приближенным значением функции cos в точке X.

while True:
    try:
        x = float(input("Введите X: "))
        break
    except ValueError:
        print("Введите вещественное число.")

while True:
    try:
        n = int(input("Введите N: "))
        if n > 0 :
            break
        print ("Число должно быть больше нуля.")
    except ValueError:
        print("Ввежите целое число.")

sum_cos = 1.0
term = 1.0
index = 1

while index <= n:
    term *= -x* x / ((2 * index - 1) * (2 * index ))
    sum_cos += term
    index += 1

print("Приближение значение cos(X):", sum_cos)


