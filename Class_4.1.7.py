# Напишите программу, которая проверяет, что для заданного четырехзначного числа
# выполняется следующее соотношение: сумма 1й и последней цифр равна разности 2й и 3й цифр.

# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.

num = int(input())
# 1834, 1234
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
if (digit1 + digit4) == (digit2 - digit3):
    print("Да")
else:
    print("Нет")