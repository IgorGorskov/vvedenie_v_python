# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input('введите число: '))
exp_two = 2
print(0)
print(exp_two)
while exp_two * 2 < n:
    exp_two *= 2
    print(exp_two)

