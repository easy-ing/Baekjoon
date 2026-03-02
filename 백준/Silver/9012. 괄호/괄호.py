import sys

def is_vps(s: str) -> bool:
    bal = 0
    for ch in s:
        if ch == '(':
            bal += 1
        else:  # ')'
            if bal == 0:
                return False
            bal -= 1
    return bal == 0

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []
    for _ in range(t):
        s = input().strip()
        out.append("YES" if is_vps(s) else "NO")
    print("\n".join(out))

if __name__ == "__main__":
    main()