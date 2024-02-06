n = int(input())
nums = list(map(int, input().split()))


def heapify(_n, i):
    largest = i
    l = i * 2 + 1
    r = (i + 1) * 2

    if l < _n and nums[l] > nums[largest]:
        largest = l

    if r < _n and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        tmp = nums[i]
        nums[i] = nums[largest]
        nums[largest] = tmp
        heapify(_n, largest)


def heap_sort():
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        tmp = nums[0]
        nums[0] = nums[i]
        nums[i] = tmp
        heapify(i - 1, 0)


heap_sort()

print(' '.join(map(str, nums)))