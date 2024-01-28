arr = input().split(' ')
a = int(arr[0])
b = int(arr[1])
c = a + b
d = c / (a - b)

print("%.2f" % (round(d * 100) / 100))