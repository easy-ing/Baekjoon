def solution(msg):
    answer = []

    # 1. 사전 초기화
    dictionary = {chr(ord('A') + i): i + 1 for i in range(26)}
    
    # 다음 사전 번호
    next_index = 27
    
    # 현재 위치
    i = 0

    while i < len(msg):
        # 현재 문자열
        w = msg[i]
        
        # 다음 글자를 붙여가며 가장 긴 문자열 찾기
        j = i + 1
        
        while j < len(msg) and w + msg[j] in dictionary:
            w += msg[j]
            j += 1
        
        # 가장 긴 문자열의 색인 번호 출력
        answer.append(dictionary[w])
        
        # 아직 처리하지 않은 글자가 있다면
        if j < len(msg):
            # w + 다음 글자를 사전에 추가
            dictionary[w + msg[j]] = next_index
            next_index += 1
        
        # 처리한 만큼 이동
        i = j

    return answer