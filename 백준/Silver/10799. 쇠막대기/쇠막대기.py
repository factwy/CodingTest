import sys

input_data = sys.stdin.readline().rstrip()
size = 0
res = 0

for index, data in enumerate(input_data):
    if data == '(':
        size += 1
    else:
        if input_data[index-1] == '(':
            res += (size - 1)
        else:
            res += 1
        size -= 1

sys.stdout.write(str(res))