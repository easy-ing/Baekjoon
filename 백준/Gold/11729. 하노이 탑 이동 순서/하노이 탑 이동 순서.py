import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def hanoi(n, frm, via, to, out):
    if n == 0:
        return
    hanoi(n-1, frm, to, via, out)
    out.append(f"{frm} {to}\n")
    hanoi(n-1, via, frm, to, out)

def main():
    n = int(input().strip())
    k = (1 << n) - 1
    out = [str(k) + "\n"]
    hanoi(n, 1, 2, 3, out)
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    main()