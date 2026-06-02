def solution(dist_limit, split_limit):
    answer = 1

    pow2 = 1

    while pow2 <= split_limit:
        pow3 = 1

        while pow2 * pow3 <= split_limit:
            leaf = pow2 * pow3

            used = (pow2 - 1) + pow2 * ((pow3 - 1) // 2)

            if used <= dist_limit:
                answer = max(answer, leaf)

                remain = dist_limit - used

                for child in [2, 3]:
                    if leaf * child <= split_limit:
                        add = min(remain, leaf)
                        answer = max(answer, leaf + add * (child - 1))

            pow3 *= 3

        pow2 *= 2

    return answer