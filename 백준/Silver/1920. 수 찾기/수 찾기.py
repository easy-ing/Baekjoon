import sys
input = sys.stdin.readline

def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return 0

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

M = int(input().strip())
queries = list(map(int, input().split()))

out = []
for x in queries:
    out.append(str(binary_search(A, x)))

sys.stdout.write("\n".join(out))