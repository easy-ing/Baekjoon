def solution(s):
    answer = ''
    new_word = True  # 단어의 시작 여부

    for char in s:
        if char == ' ':
            answer += char
            new_word = True
        else:
            if new_word:
                answer += char.upper()
                new_word = False
            else:
                answer += char.lower()

    return answer