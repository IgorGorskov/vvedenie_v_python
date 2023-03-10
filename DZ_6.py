# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

num = input('введите норме билета \n')
sum_left = 0
sum_right = 0
for i in range(3):
    sum_left += int(num[i])
for i in range(3,6):
    sum_right += int(num[i])
if sum_left == sum_right: print('yes')
else: print('no')