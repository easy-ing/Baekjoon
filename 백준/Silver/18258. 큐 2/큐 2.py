import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    q = deque()
    out = []

    for _ in range(n):
        cmd = input().split()

        if cmd[0] == "push":
            q.append(int(cmd[1]))

        elif cmd[0] == "pop":
            out.append(str(q.popleft() if q else -1))

        elif cmd[0] == "size":
            out.append(str(len(q)))

        elif cmd[0] == "empty":
            out.append("1" if not q else "0")

        elif cmd[0] == "front":
            out.append(str(q[0] if q else -1))

        elif cmd[0] == "back":
            out.append(str(q[-1] if q else -1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()