def solution(m, musicinfos):
    # #이 붙은 음을 한 글자로 변환
    change = {
        'C#': 'c',
        'D#': 'd',
        'F#': 'f',
        'G#': 'g',
        'A#': 'a'
    }

    def convert(melody):
        for before, after in change.items():
            melody = melody.replace(before, after)
        return melody

    m = convert(m)

    answer = '(None)'
    max_time = -1

    for info in musicinfos:
        start, end, title, melody = info.split(',')

        # 재생 시간 계산
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))

        time = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        # 악보 변환
        melody = convert(melody)

        # 실제 재생된 멜로디 만들기
        repeat = time // len(melody)
        remain = time % len(melody)

        played = melody * repeat + melody[:remain]

        # 기억한 멜로디가 실제 재생된 곡에 포함되는지 확인
        if m in played:
            if time > max_time:
                max_time = time
                answer = title

    return answer