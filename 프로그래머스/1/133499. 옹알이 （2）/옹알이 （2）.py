def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        index = 0
        previous = ""

        while index < len(word):
            found = False

            for sound in sounds:
                if sound != previous and word.startswith(sound, index):
                    index += len(sound)
                    previous = sound
                    found = True
                    break

            if not found:
                break

        if index == len(word):
            answer += 1

    return answer