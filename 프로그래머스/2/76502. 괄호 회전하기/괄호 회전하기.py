def solution(s):
    answer = 0

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    n = len(s)

    for x in range(n):
        rotated = s[x:] + s[:x]
        stack = []

        for ch in rotated:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    break

                stack.pop()
        else:
            if not stack:
                answer += 1

    return answer