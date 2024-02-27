stack = []
chars = input()

for char in chars:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if len(stack) == 0:
            print('No')
            quit()
        stack.pop()

print('Yes' if len(stack) == 0 else 'No')