n = int(input())
first = None
last = None

for i in range(n):
    if first is None:
        first = [i + 1, None, None]
        last = first
        continue

    curr = [i + 1, last, None]
    last[2] = curr
    last = curr

while first is not None and last is not None and first[0] != last[0]:
    first = first[2]
    first[1] = None

    first[1] = last
    last[2] = first
    last = first
    first = first[2]

print(first[0])