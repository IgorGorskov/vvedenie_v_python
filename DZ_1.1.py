# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите число \n'))
sum = 0
for i in range(2):
    sum += n % 10
    n //= 10
print(sum + n)