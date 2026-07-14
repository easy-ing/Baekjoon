def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]

    for i, correct_answer in enumerate(answers):
        for student in range(3):
            pattern = patterns[student]

            if correct_answer == pattern[i % len(pattern)]:
                scores[student] += 1

    max_score = max(scores)

    answer = []

    for student, score in enumerate(scores):
        if score == max_score:
            answer.append(student + 1)

    return answer