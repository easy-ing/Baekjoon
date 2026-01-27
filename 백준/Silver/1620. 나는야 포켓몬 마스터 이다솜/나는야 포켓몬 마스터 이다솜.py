import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_to_name = [""] * (n + 1)
name_to_num = {}

for i in range(1, n + 1):
    name = input().strip()
    num_to_name[i] = name
    name_to_num[name] = i

out = []
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        out.append(num_to_name[int(q)])
    else:
        out.append(str(name_to_num[q]))

print("\n".join(out))