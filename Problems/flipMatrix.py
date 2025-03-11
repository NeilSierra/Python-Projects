lenght = int(input("Enter matrix lenght: "))
height = int(input("Enter matrix height: "))

matrix = {}

for i in range(height):
    nums = list(map(int, input().split()))[:lenght]
    matrix[i] = nums

print("\nFlipped matrix: ")
for i in range(lenght):
    for list in matrix.values():
        print(list[i], end=" ")
    print()