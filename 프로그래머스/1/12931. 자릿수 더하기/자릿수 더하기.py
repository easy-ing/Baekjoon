def solution(n):
    answer = 0
    while(n>0):
        
        sub = n%10
        answer = answer + sub
        n = n//10

    return answer