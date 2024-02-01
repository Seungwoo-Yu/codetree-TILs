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
        if _end - _start >= 3:
            pos = pivot(_nums, _start, _end)
            if pos < _end:
                tmp = _nums[_end]
                _nums[_end] = _nums[pos]
                _nums[pos] = tmp

        pos = sort(_nums, _start, _end)
        quick_sort(_nums, _start, pos - 1)
        quick_sort(_nums, pos + 1, _end)


def sort(_nums, _start, _end):
    pvt = _nums[_end]
    i = _start - 1

    for j in range(_start, _end):
        if _nums[j] < pvt:
            i += 1
            tmp = _nums[i]
            _nums[i] = _nums[j]
            _nums[j] = tmp

    tmp = _nums[i + 1]
    _nums[i + 1] = _nums[_end]
    _nums[_end] = tmp

    return i + 1


quick_sort(nums, 0, len(nums) - 1)
print(' '.join(map(str, nums)))