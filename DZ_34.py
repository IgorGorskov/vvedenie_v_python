phraces = input('Введите стих: ').split(' ')  
count_first = phraces[0].count('а')
flag = True
for i in phraces:
    if i.count('а') != count_first:
        flag = False
        print('Пам парам')
        break
if flag: print("Парам пам-пам")