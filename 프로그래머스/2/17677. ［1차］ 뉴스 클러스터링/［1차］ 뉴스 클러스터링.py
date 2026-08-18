from collections import Counter

def solution(str1, str2):
    def make_set(s):
        s = s.lower()
        result = []

        for i in range(len(s) - 1):
            word = s[i:i + 2]

            if word.isalpha():
                result.append(word)

        return Counter(result)

    c1 = make_set(str1)
    c2 = make_set(str2)

    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())

    if union == 0:
        return 65536

    return int(intersection / union * 65536)