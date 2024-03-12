[n, k] = list(map(int, input().split()))
first = None
last = None

for i in map(lambda x: x + 1, range(n)):
    if first is None:
        first = [i, None]
        last = first
        continue

    curr = [i, first]
    last[1] = curr
    last = curr

while last is not None:
    if first is not None and last[0] == first[0]:
        print(last[0], end='')
        break

    for _ in range(k - 1):
        last = first
        first = first[1]

    print(first[0], end=' ')
    printing = True
    first = first[1]
    last[1] = first