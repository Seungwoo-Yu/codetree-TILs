n = int(input())
first = None
last = None
_len = 0

for i in range(n):
    arg = input().split()

    if arg[0] == 'push_front':
        _len += 1
        if first is None or _len == 1:
            first = [int(arg[1]), None, None]
            last = first
            continue

        curr = [int(arg[1]), None, first]
        first[1] = curr
        first = curr

    if arg[0] == 'push_back':
        _len += 1
        if first is None or _len == 1:
            first = [int(arg[1]), None, None]
            last = first
            continue

        curr = [int(arg[1]), last, None]
        last[2] = curr
        last = curr

    if arg[0] == 'pop_front':
        _len -= 1
        value = first[0]
        first = first[2]
        print(value)

        if _len == 0:
            last = None

    if arg[0] == 'pop_back':
        _len -= 1
        value = last[0]
        last = last[1]
        print(value)

        if _len == 0:
            first = None

    if arg[0] == 'size':
        print(_len)

    if arg[0] == 'empty':
        print('1' if _len == 0 else '0')

    if arg[0] == 'front':
        print(first[0])

    if arg[0] == 'back':
        print(last[0])