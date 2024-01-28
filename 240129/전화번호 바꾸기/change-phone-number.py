arr = input().split('-')
tmp = arr[1]
arr[1] = arr[2]
arr[2] = tmp

print(f"{'-'.join(arr)}")