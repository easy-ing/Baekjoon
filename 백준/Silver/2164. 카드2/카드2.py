import sys

N = int(sys.stdin.readline().strip())
L = 1 << (N.bit_length() - 1)

if N == L:
    print(N)
else:
    print(2 * (N - L))