bushes = [int(i) for i in input('Введите через пробел число ягод на каждом кусте: ').split()]
MaxSum = bushes[0] + bushes[1] + bushes[2]
for i in range(len(bushes) - 1):
    print(f'Check{i}')
    if MaxSum < bushes[i - 1] + bushes[i] + bushes[i + 1]: 
        MaxSum = bushes[i - 1] + bushes[i] + bushes[i + 1]
if MaxSum < bushes[len(bushes) - 1] + bushes[len(bushes) - 2] + bushes[0]:
    MaxSum = bushes[len(bushes) - 1] + bushes[len(bushes) - 2] + bushes[0]
print(MaxSum)