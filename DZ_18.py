n = int(input('введите количество элементов массива: '))
array = input('введите массив: ').split()
x = int(input('введтие х: '))
modul = 100000000000000000
for i in array:
    if abs(x - int(i)) < modul: answer = i
print(answer)