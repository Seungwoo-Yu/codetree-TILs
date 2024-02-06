n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, -1)

def heapify(_n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= _n and nums[l] > nums[largest]:
        largest = l

    if r <= _n and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        tmp = nums[i]
        nums[i] = nums[largest]
        nums[largest] = tmp
        heapify(_n, largest)


def heap_sort():
    for i in range((n - 1) // 2 + 1, 0, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        tmp = nums[1]
        nums[1] = nums[i + 1]
        nums[i + 1] = tmp
        heapify(i - 1, 1)


heap_sort()
del nums[0]

print(' '.join(map(str, nums)))