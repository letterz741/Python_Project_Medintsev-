#Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^N.
n = int(input( "N (>0) = "))

total = 0
for i in range (1, n + 1):
    total += i ** i
print("Сумма:", total)