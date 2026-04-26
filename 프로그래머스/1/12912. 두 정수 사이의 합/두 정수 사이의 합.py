def solution(a, b):
    start = min(a, b)
    end = max(a, b)

    count = end - start + 1
    return (start + end) * count // 2