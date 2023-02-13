n  = int(input('Введите кол-во элементов 1 множества: '))
m  = int(input('Введите кол-во элементов 2 множества: '))
list_1 = [int(i)  for i in input('Введите элементы 1 множества одной строкой через пробел: ').split()]
if len(list_1) != n: print('Неточность: количество элементов не соответсвует заявленому')
list_2 = [int(i) for i in input('Введите элементы 2 множества одной строкой через пробел: ').split()]
if len(list_2) != m: print('Неточность: количество элементов не соответсвует заявленому')

list_result = list()

for i in list_1:
    for j in list_2:
        if i == j and i not in list_result: list_result.append(i)
list_result.sort()
print(*list_result)
