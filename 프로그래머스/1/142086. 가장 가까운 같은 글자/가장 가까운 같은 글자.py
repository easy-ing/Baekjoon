def solution(s):
    answer = []
    last_index = {}

    for i, char in enumerate(s):
        if char in last_index:
            answer.append(i - last_index[char])
        else:
            answer.append(-1)

        last_index[char] = i

    return answer