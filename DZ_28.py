def sm(a, b):
    if b == 0: return a
    return 1 + sm(a, b - 1)

a = int(input('введите число а: '))
b = int(input('введите число b: '))
print(sm(a,b))
