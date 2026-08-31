def solution(number, k):
    stack = []

    for num in number:
        # 현재 숫자가 더 크다면
        # 앞의 작은 숫자를 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    # 아직 제거해야 할 숫자가 남았다면
    # 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)