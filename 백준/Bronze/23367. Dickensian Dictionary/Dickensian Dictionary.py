import sys

left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}

data = sys.stdin.readline().rstrip()

isLeft = False

if data[0] in left:
    isLeft = True
else:
    isLeft = False

isDickensian = True

for word in data[1:]:
    if isLeft:
        if word not in left:
            isLeft = False
        else:
            isDickensian = False
            break
    else:
        if word in left:
            isLeft = True
        else:
            isDickensian = False
            break

if isDickensian:
    print("yes")
else:
    print("no")
