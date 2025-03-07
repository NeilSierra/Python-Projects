while True:
  size = int(input("Enter size: "))
  if size % 2 == 1:
    break
  print("Please enter an odd number.")
print()

for x in range(size):
  row = [" "] * size
  row[x] = "x"
  row[size - x - 1] = "x"
  print(" ".join(row))
print()

median = size // 2 + 1
for y in range(size):
  row = [" "] * size
  if y < median:
    row[y] = "y"
    row[size - y - 1] = "y"
  else:
    row[size - y - 1] = "y"
  print(" ".join(row))
print()

for z in range(size):
  if z == 0 or z == size - 1:
    row = ["z"] * size
  else:
    row = [" "] * size
    row[size - z - 1] = "z"
  print(" ".join(row))
print()