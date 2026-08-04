def solution(message, spoiler_ranges):
    words = []

    # 단어 파싱
    i = 0
    while i < len(message):
        if message[i] == ' ':
            i += 1
            continue

        start = i
        while i < len(message) and message[i] != ' ':
            i += 1
        end = i - 1

        words.append({
            "text": message[start:i],
            "start": start,
            "end": end,
            "spoiler": False
        })

    # 스포 단어 표시
    r = 0
    for word in words:
        while r < len(spoiler_ranges) and spoiler_ranges[r][1] < word["start"]:
            r += 1

        if r < len(spoiler_ranges):
            s, e = spoiler_ranges[r]
            if word["start"] <= e and word["end"] >= s:
                word["spoiler"] = True

    # 일반 영역 단어
    normal_words = set()
    for word in words:
        if not word["spoiler"]:
            normal_words.add(word["text"])

    answer = 0
    revealed = set()

    # 스포 클릭 순서대로
    idx = 0
    for s, e in spoiler_ranges:
        while idx < len(words) and words[idx]["end"] < s:
            idx += 1

        j = idx
        while j < len(words) and words[j]["start"] <= e:
            text = words[j]["text"]

            if text not in normal_words and text not in revealed:
                answer += 1
                revealed.add(text)

            j += 1

    return answer