num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    print("YES")
else:
    print("NO")
