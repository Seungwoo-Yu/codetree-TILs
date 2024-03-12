n = int(input())
first = None
last = None

for i in range(n):
    if first is None:
        first = [i + 1, None]
        last = first
        continue

    curr = [i + 1, None]
    last[1] = curr
    last = curr

while first is not None and last is not None and first[0] != last[0]:
    first = first[1]

    last[1] = first
    last = first
    first = first[1]

print(first[0])