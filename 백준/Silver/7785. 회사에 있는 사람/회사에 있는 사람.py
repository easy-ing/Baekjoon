import sys
input = sys.stdin.readline

n = int(input())
inside = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        inside.add(name)
    else:  # leave
        inside.remove(name)

print("\n".join(sorted(inside, reverse=True)))