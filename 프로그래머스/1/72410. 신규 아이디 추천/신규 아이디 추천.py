def solution(new_id):
    # 1단계: 대문자를 소문자로 변경
    new_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = "".join(char for char in new_id if char in allowed)

    # 3단계: 연속된 마침표를 하나로 변경
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip(".")

    # 5단계: 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = "a"

    # 6단계: 길이가 16 이상이면 15자까지만 자르기
    new_id = new_id[:15]

    # 자른 뒤 마지막 문자가 마침표라면 제거
    new_id = new_id.rstrip(".")

    # 7단계: 길이가 3이 될 때까지 마지막 문자 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id