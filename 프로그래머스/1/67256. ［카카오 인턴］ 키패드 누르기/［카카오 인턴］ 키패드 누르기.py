def solution(numbers, hand):
    answer = ""

    left_position = "*"
    right_position = "#"

    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        "*": (3, 0), 0: (3, 1), "#": (3, 2)
    }

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_position = number

        elif number in [3, 6, 9]:
            answer += "R"
            right_position = number

        else:
            number_row, number_col = keypad[number]
            left_row, left_col = keypad[left_position]
            right_row, right_col = keypad[right_position]

            left_distance = abs(number_row - left_row) + abs(number_col - left_col)
            right_distance = abs(number_row - right_row) + abs(number_col - right_col)

            if left_distance < right_distance:
                answer += "L"
                left_position = number

            elif left_distance > right_distance:
                answer += "R"
                right_position = number

            else:
                if hand == "left":
                    answer += "L"
                    left_position = number
                else:
                    answer += "R"
                    right_position = number

    return answer