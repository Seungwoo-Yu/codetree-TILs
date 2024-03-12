n = int(input())
first = None
last = None
_len = 0

for i in range(n):
    arg = input().split()

    if arg[0] == 'push':
        _len += 1
        if first is None:
            first = [int(arg[1]), None]
            last = first
            continue

        curr = [int(arg[1]), None]
        last[1] = curr
        last = curr

    if arg[0] == 'pop':
        _len -= 1
        value = first[0]
        first = first[1]
        print(value)

    if arg[0] == 'size':
        print(_len)

    if arg[0] == 'empty':
        print('1' if _len == 0 else '0')

    if arg[0] == 'front':
        print(first[0])