num = int(input())
num1 = num // 100 
num2 = (num % 100) // 10
num3 = (num % 1000) // 100
num4 = num % 10
print(f"{num1}{num2}{num3}{num4}")
