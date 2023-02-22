a1 = int(input('Введите первый член прогрессии: '))
list1 = [a1]
d = int(input('Введите разность прогрессии: '))
n = int(input('Введите кол-во членов прогрессии: '))
for i in range(1, n):
    list1.append(list1[i - 1] + d)
print(*list1)