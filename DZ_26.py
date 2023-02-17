a = int(input('введите число а: '))
b = int(input('введите число b: '))
def pw(a, b):
    if b == 0: return 1
    return a * pw(a, b - 1)
print(pw(a, b))