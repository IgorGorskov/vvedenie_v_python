def pw(a, b):
    if b == 0: return 1
    return a * pw(a, b - 1)

a = int(input('введите число а: '))
b = int(input('введите число b: '))
print(pw(a, b))