def solution(n, words):
    used = set()
    for i, word in enumerate(words):
        # 첫 번째 단어가 아니라면 끝말잇기 규칙 검사
        if i > 0 and words[i - 1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        # 이미 사용한 단어인지 검사
        if word in used:
            return [i % n + 1, i // n + 1]
        used.add(word)
    # 모든 단어가 규칙을 지킨 경우
    return [0, 0]