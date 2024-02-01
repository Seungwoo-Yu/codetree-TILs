n = int(input())
nums = list(map(int, input().split()))


def merge_sort(_nums, _min, _max):
    if _min < _max:
        med = (_min + _max) // 2
        merge_sort(_nums, _min, med)
        merge_sort(_nums, med + 1, _max)
        merge(_nums, _min, med, _max)


temp = [None] * len(nums)


def merge(_nums, _min, _med, _max):
    i = _min
    j = _med + 1
    k = _min

    while i <= _med and j <= _max:
        if _nums[i] < _nums[j]:
            temp[k] = _nums[i]
            k += 1
            i += 1
        else:
            temp[k] = _nums[j]
            k += 1
            j += 1

    while i <= _med:
        temp[k] = _nums[i]
        k += 1
        i += 1

    while j <= _max:
        temp[k] = _nums[j]
        k += 1
        j += 1

    for k in range(_min, _max + 1):
        _nums[k] = temp[k]


merge_sort(nums, 0, len(nums) - 1)
print(' '.join(map(str, nums)))