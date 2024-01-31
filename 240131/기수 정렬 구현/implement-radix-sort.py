n = int(input())
nums = list(input().split())
k = max(len(num) for num in nums)

for i in range(k):
    sort = [[] for _ in range(10)]

    for j in range(len(nums)):
        digit = int(nums[j][i] or '0')
        sort[digit].append(nums[j])

    result = list()

    for j in range(len(sort)):
        for k in range(len(sort[j])):
            result.append(sort[j][k])

    nums = result

print(' '.join(nums))