import sys

def main():
    input = sys.stdin.readline
    k = int(input().strip())
    stack = []

    for _ in range(k):
        x = int(input().strip())
        if x == 0:
            stack.pop()
        else:
            stack.append(x)

    print(sum(stack))

if __name__ == "__main__":
    main()