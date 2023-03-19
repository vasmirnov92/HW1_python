# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите число: ')
number = input()
number = int(number)

summOfDigits = 0
while number != 0:
    summOfDigits = summOfDigits + number%10
    number = number // 10

print('Сумма цифр в числе равна: ')
print(summOfDigits)