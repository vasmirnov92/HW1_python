# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print('Счастливый ли билет?')
print('Введите номер билета')
number = input()
number = int(number)
# print(number)

leftThree = number//1000
# print(leftThree)
leftSummOfDigits = 0
rightThree = number%1000
# print(rightThree)
rightSummOfDigits = 0



while rightThree != 0:
    rightSummOfDigits = rightSummOfDigits + rightThree%10
    rightThree = rightThree//10

while leftThree != 0:
    leftSummOfDigits = leftSummOfDigits + leftThree%10
    leftThree = leftThree//10


# print(rightSummOfDigits)
# print(leftSummOfDigits)
# print(leftSummOfDigits == rightSummOfDigits)

if leftSummOfDigits == rightSummOfDigits:
    print('YES')
else:
    print('NO')


