import sys

def balanced(line: str) -> bool:
    st = []
    for ch in line:
        if ch == '(' or ch == '[':
            st.append(ch)
        elif ch == ')':
            if not st or st[-1] != '(':
                return False
            st.pop()
        elif ch == ']':
            if not st or st[-1] != '[':
                return False
            st.pop()
    return not st

def main():
    input = sys.stdin.readline
    out = []
    while True:
        line = input()
        if not line:
            break
        line = line.rstrip('\n')
        if line == '.':
            break
        out.append('yes' if balanced(line) else 'no')
    print('\n'.join(out))

if __name__ == "__main__":
    main()