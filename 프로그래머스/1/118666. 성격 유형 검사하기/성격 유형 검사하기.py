def solution(survey, choices):
    scores = {char: 0 for char in "RTCFJMAN"}

    for types, choice in zip(survey, choices):
        if choice < 4:
            scores[types[0]] += 4 - choice
        elif choice > 4:
            scores[types[1]] += choice - 4

    answer = ""

    for first, second in ["RT", "CF", "JM", "AN"]:
        if scores[first] >= scores[second]:
            answer += first
        else:
            answer += second

    return answer