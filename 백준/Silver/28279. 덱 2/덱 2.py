import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()
result = []

for _ in range(n):
    command = input().split()
    cmd = int(command[0])

    if cmd == 1:
        dq.appendleft(int(command[1]))
    elif cmd == 2:
        dq.append(int(command[1]))
    elif cmd == 3:
        result.append(str(dq.popleft()) if dq else "-1")
    elif cmd == 4:
        result.append(str(dq.pop()) if dq else "-1")
    elif cmd == 5:
        result.append(str(len(dq)))
    elif cmd == 6:
        result.append("1" if not dq else "0")
    elif cmd == 7:
        result.append(str(dq[0]) if dq else "-1")
    elif cmd == 8:
        result.append(str(dq[-1]) if dq else "-1")

print("\n".join(result))