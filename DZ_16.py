n = int(input('введите количество элементов массива: '))
array = input('введите массив: ').split()
x = input('введтие х:')
counter = 0
for i in array:
    if x == i: counter += 1
print(f'число х содержится в массиве {counter} раз.')