def solution(n, l, r):
    def count_ones(x, level):
        if x <= 0:
            return 0
        if level == 0:
            return 1

        length = 5 ** (level - 1)
        ones = 4 ** (level - 1)

        block = x // length
        remain = x % length

        count = 0

        for i in range(min(block, 5)):
            if i != 2:
                count += ones

        if block >= 5:
            count = 4 * ones

        if block < 5 and block != 2:
            count += count_ones(remain, level - 1)

        return count

    return count_ones(r, n) - count_ones(l - 1, n)