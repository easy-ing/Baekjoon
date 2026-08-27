def solution(files):
    parsed = []

    for file in files:
        # NUMBER가 시작되는 위치 찾기
        head_end = 0

        while not file[head_end].isdigit():
            head_end += 1

        # HEAD
        head = file[:head_end].lower()

        # NUMBER가 끝나는 위치 찾기
        number_end = head_end

        while number_end < len(file) and file[number_end].isdigit():
            number_end += 1

        # NUMBER
        number = int(file[head_end:number_end])

        parsed.append((head, number, file))

    # HEAD → NUMBER 순으로 정렬
    # Python의 sort는 stable sort이므로
    # HEAD와 NUMBER가 같으면 기존 순서가 유지됨
    parsed.sort(key=lambda x: (x[0], x[1]))

    return [file for _, _, file in parsed]