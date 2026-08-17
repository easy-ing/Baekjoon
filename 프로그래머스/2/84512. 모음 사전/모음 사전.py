def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']

    def dfs(current):
        if len(current) > 5:
            return

        if current:
            words.append(current)

        for vowel in vowels:
            dfs(current + vowel)

    dfs("")

    return words.index(word) + 1