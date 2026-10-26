def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = [(begin, 0)]
    head = 0

    while head < len(queue):
        word, steps = queue[head]
        head += 1

        if word == target:
            return steps

        for i in range(len(words)):
            if visited[i]:
                continue

            diff = 0

            for j in range(len(word)):
                if word[j] != words[i][j]:
                    diff += 1

            if diff == 1:
                visited[i] = True
                queue.append((words[i], steps + 1))

    return 0