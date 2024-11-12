num1 = input()
num2 = input()
num3 = input()
num4 = input()
if num1 <= num2:
    a = num1
if num2 <= num1:
    a = num2
if num3 <= num4:
    b = num3
if num4 <= num3:
    b = num4
if a < b:
    print(a)
else:
    print(b)
