import sys

input_a = sys.stdin.readline().rstrip().split("/")
input_b = sys.stdin.readline().rstrip().split("/")

start, end = 0, 0
len_a, len_b = len(input_a), len(input_b)

while start < len_a and start < len_b:
    if len_a - end - 1 < 0 or len_a - end - 1 >= len_a:
        break
    if len_b - end - 1 < 0 or len_b - end - 1 >= len_b:
        break

    check = True
    if input_a[start] == input_b[start]:
        start += 1
        check = False

    if input_a[len_a - end - 1] == input_b[len_b - end - 1]:
        end += 1
        check = False

    if check:
        break

first = input_a[:start]

mid_a = input_a[start:len_a-end]
mid_b = input_b[start:len_b-end]

last = input_b[len_b-end:]


for w in first:
    sys.stdout.write(w + '/')
sys.stdout.write("{")
for index, w in enumerate(mid_a):
    if index > 0:
        sys.stdout.write("/")
    sys.stdout.write(w)
sys.stdout.write(" => ")
for index, w in enumerate(mid_b):
    if index > 0:
        sys.stdout.write("/")
    sys.stdout.write(w)
sys.stdout.write("}")
for w in last:
    sys.stdout.write("/" + w)