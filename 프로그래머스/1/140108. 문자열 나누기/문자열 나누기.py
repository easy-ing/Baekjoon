def solution(s):
    answer = 0
    x_count = 0
    other_count = 0
    x = ''
    
    for char in s:
        if x_count == 0:
            x = char
        
        if char == x:
            x_count += 1
        else:
            other_count += 1
        
        if x_count == other_count:
            answer += 1
            x_count = 0
            other_count = 0
    
    if x_count != 0:
        answer += 1
    
    return answer