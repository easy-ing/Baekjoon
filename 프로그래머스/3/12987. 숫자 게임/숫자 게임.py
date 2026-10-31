def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    a = 0

    for b in range(len(B)):
        if B[b] > A[a]:
            answer += 1
            a += 1

    return answer