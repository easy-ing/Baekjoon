import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

minus_one = 0
zero = 0
one = 0

def divide(x, y, size):
    global minus_one, zero, one

    first = paper[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        if first == -1:
            minus_one += 1
        elif first == 0:
            zero += 1
        else:
            one += 1
        return

    new_size = size // 3

    for dx in range(3):
        for dy in range(3):
            divide(x + dx * new_size, y + dy * new_size, new_size)

divide(0, 0, n)

print(minus_one)
print(zero)
print(one)