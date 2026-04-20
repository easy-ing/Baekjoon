def solution(s):
    transform_count = 0
    removed_zero_count = 0

    while s != "1":
        zero_count = s.count('0')
        removed_zero_count += zero_count

        one_count = len(s) - zero_count
        s = bin(one_count)[2:]

        transform_count += 1

    return [transform_count, removed_zero_count]