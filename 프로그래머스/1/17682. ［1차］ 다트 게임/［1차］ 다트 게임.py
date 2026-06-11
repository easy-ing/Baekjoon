def solution(dartResult):
    scores = []
    i = 0

    while i < len(dartResult):
        if dartResult[i].isdigit():
            if i + 1 < len(dartResult) and dartResult[i + 1].isdigit():
                score = int(dartResult[i:i+2])
                i += 2
            else:
                score = int(dartResult[i])
                i += 1

            bonus = dartResult[i]

            if bonus == "S":
                score = score ** 1
            elif bonus == "D":
                score = score ** 2
            elif bonus == "T":
                score = score ** 3

            scores.append(score)
            i += 1

        else:
            if dartResult[i] == "*":
                scores[-1] *= 2

                if len(scores) >= 2:
                    scores[-2] *= 2

            elif dartResult[i] == "#":
                scores[-1] *= -1

            i += 1

    return sum(scores)