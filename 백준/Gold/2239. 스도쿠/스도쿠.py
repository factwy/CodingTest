import sys
numbers = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def backtracking(index, size):
    if index == size:
        return True

    x, y = need_to_write[index]
    number = 1
    space_index = x//3*3 + y//3

    while number <= 9:
        if numbers[number] in set_row[x] or numbers[number] in set_col[y] or numbers[number] in set_space[space_index]:
            number += 1
            continue

        set_row[x].add(numbers[number])
        set_col[y].add(numbers[number])
        set_space[space_index].add(numbers[number])
        graph[x][y] = numbers[number]

        if backtracking(index+1, size):
            return True
        set_row[x].remove(numbers[number])
        set_col[y].remove(numbers[number])
        set_space[space_index].remove(numbers[number])

        number += 1

    return False


need_to_write = []
set_row = [set() for _ in range(9)]
set_col = [set() for _ in range(9)]
set_space = [set() for _ in range(9)]
graph = [list(sys.stdin.readline().rstrip()) for _ in range(9)]

for x in range(9):
    for y in range(9):
        if graph[x][y] == '0':
            need_to_write.append((x, y))
        else:
            set_row[x].add(graph[x][y])
            set_col[y].add(graph[x][y])
            set_space[x//3*3 + y//3].add(graph[x][y])

size = len(need_to_write)
backtracking(0, size)

for g in graph:
    sys.stdout.write(''.join(g) + '\n')
