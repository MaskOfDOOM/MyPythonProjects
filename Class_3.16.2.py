num = int(input())
num1 = num // 1000
num2 = (num % 1000) // 100
num3 = (num % 100) // 10
num4 = num % 10
print(f"Цифра в позиции тысяч равна {num1}")
print(f"Цифра в позиции сотен равна {num2}")
print(f"Цифра в позиции десятков равна {num3}")
print(f"Цифра в позиции единиц равна {num4}")
