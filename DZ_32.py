mx = int(input('Введите максимум: '))
mn = int(input('Введите минимум: '))
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_ans = list()
for i in range(len(list1)):
    if mn <= list1[i] <= mx:
        list_ans.append(i)
print(*list_ans)