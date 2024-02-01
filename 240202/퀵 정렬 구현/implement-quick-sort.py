n = int(input())
nums = list(map(int, input().split()))


def pivot(_nums, _start, _end):
    med = (_start + _end) // 2
    nominated = [_nums[_start], _nums[med], _nums[_end]]
    nominated.sort()

    if nominated[1] == _nums[_start]:
        return _start

    if nominated[1] == _nums[med]:
        return med

    return _end


def quick_sort(_nums, _start, _end):
    if _start < _end:
        if len(_nums) >= 3:
            pos = pivot(_nums, _start, _end)
            if pos < _end:
                tmp = _nums[_end]
                _nums[_end] = _nums[pos]
                _nums[pos] = tmp

        post = sort(_nums, _start, _end)
        quick_sort(_nums, _start, post - 1)
        quick_sort(_nums, post + 1, _end)


def sort(_nums, _start, _end):
    pvt = _nums[_end]
    i = 0
    j = 0

    while j < len(_nums):
        if _nums[i] < pvt:
            i += 1
            j += 1

        if _nums[j] > pvt:
            j += 1
        elif _nums[i] >= pvt:
            tmp = _nums[i]
            _nums[i] = _nums[j]
            _nums[j] = tmp
            i += 1
            j += 1

    if j < len(_nums):
        tmp = _nums[i]
        _nums[i] = _nums[_end]
        _nums[_end] = tmp

    return i


quick_sort(nums, 0, len(nums) - 1)
print(' '.join(map(str, nums)))