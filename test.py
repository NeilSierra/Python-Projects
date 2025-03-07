nums =  [5, 10, 2, 1, 20, 4]

lis = [1] * len(nums)
print(lis)

for i in range(len(nums)-1, -1, -1):
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            lis[i] = max(lis[i], lis[j]+1)
result = max(lis)

print(result)