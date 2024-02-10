n = int(input())
stack = []

for i in range(n):
    arg = input().split()

    if arg[0] == 'push':
        stack.append(arg[1])

    if arg[0] == 'pop':
        print(stack.pop())

    if arg[0] == 'size':
        print(len(stack))

    if arg[0] == 'empty':
        print('1' if len(stack) == 0 else '0')

    if arg[0] == 'top':
        print(stack[-1])