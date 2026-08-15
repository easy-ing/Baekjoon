from collections import deque

def solution(priorities, location):
    queue = deque((idx, priority) for idx, priority in enumerate(priorities))

    order = 0

    while queue:
        idx, priority = queue.popleft()

        if any(priority < p for _, p in queue):
            queue.append((idx, priority))
        else:
            order += 1

            if idx == location:
                return order