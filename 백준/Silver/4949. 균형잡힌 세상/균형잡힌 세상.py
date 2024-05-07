import sys

input_data = sys.stdin.readline().rstrip()
while input_data != ".":
    stack = []
    for data in input_data:
        if data == '(' or data == "[":
            stack.append(data)
        elif data == ')':
            if stack:
                op = stack.pop()
                if op != '(':
                    stack.append(op)
                    break
            else:
                stack.append(data)
                break
        elif data == ']':
            if stack:
                op = stack.pop()
                if op != '[':
                    stack.append(op)
                    break
            else:
                stack.append(data)
                break

    if stack:
        sys.stdout.write(str("no") + '\n')
    else:
        sys.stdout.write(str("yes") + '\n')

    input_data = sys.stdin.readline().rstrip()