# num%10-последняя цифра.
# (num%100)//10=средняя цифра (в трёхзначном числе).
# num//100=первая цифра.

num = int(input())
#135
num1 = num // 100
num2 = (num % 100) // 10
num3 = num % 10
sum = num1 + num2 + num3
prodnum = num1 * num2 * num3
print(f"Сумма цифр = {sum}")
print(f"Произведение цифр = {prodnum}")
