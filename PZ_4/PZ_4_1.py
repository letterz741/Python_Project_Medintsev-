#Приближене значение cos(x)
x = float(input("X ="))
n = int(input("N (>0) = "))

term = 1.0  # текущий член ряда
s = 1.0 # сумма
for k in range (1, n + 1 ):
    term *= -x * x / ((2 * k -1) * (2 * k))
    s += term
print ("Приблежение значение cos (X) :", s)    



