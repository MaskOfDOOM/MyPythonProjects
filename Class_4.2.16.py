# Ход короля
current_x = int(input())
current_y = int(input())
target_x = int(input())
target_y = int(input())
if (
    current_x + 1 == target_x or current_x - 1 == target_x or current_x == target_x
) and (current_y + 1 == target_y or current_y - 1 == target_y or current_y == target_y):
    print("YES")
else:
    print("NO")
