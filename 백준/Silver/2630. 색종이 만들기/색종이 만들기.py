import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def cut(x, y, size):
    global white, blue
    
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
        if first == 0:
            white += 1
        else:
            blue += 1
        return
    
    half = size // 2
    cut(x, y, half)                 # 1사분면
    cut(x, y + half, half)          # 2사분면
    cut(x + half, y, half)          # 3사분면
    cut(x + half, y + half, half)   # 4사분면

cut(0, 0, n)

print(white)
print(blue)