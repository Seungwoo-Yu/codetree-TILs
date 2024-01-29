n = int(input())
vals = []

for i in range(n):
    arr = input().split(' ')
    cmd = arr[0]

    if len(arr) > 1:
        val = int(arr[1])

    if cmd == 'push_back':
        vals.append(val)

    if cmd == 'pop_back':
        vals.pop()

    if cmd == 'size':
        print(len(vals))

    if cmd == 'get':
        print(vals[val - 1])