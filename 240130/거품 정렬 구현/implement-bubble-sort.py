n = int(input())
nums = list(map(int, input().split()))
sort = True

while sort:
    sort = False

    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            sort = True
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp

print(' '.join(map(str, nums)))