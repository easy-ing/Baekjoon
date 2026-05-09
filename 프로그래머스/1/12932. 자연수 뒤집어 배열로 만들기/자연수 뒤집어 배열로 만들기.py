def solution(n):
    answer = []
    while (n>0):
        sub = n % 10
        answer.append(sub)
        n = n//10
    return answer