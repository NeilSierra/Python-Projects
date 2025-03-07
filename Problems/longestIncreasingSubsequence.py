num_list = [3, 10, 2, 1, 20, 4]

data = {}

for idx, num in enumerate(num_list):
    data[idx] = [x for y, x in enumerate(num_list) if x >= num and y >= idx]

for val in data.values():
    for i, n in enumerate(val):
        if i != 0 and val[i] < val[i-1]:
            val.remove(val[i])

longest = 0
for k, v in data.items():
    if len(v) > longest:
        longest = len(v)
        long_key = k

print(data)
print()
print(longest)
print(data[long_key])