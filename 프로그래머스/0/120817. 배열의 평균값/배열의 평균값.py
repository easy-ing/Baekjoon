def solution(numbers):
    answer = 0
    length = len(numbers)
    
    for i in range(0,length):
        answer = answer + numbers[i]
    
    answer = (answer/length)
    
    return answer