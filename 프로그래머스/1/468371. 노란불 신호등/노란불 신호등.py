from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    limit = 1

    for g, y, r in signals:
        limit = lcm(limit, g + y + r)

    for t in range(1, limit + 1):
        ok = True

        for g, y, r in signals:
            cycle = g + y + r
            pos = (t - 1) % cycle + 1

            if not (g < pos <= g + y):
                ok = False
                break

        if ok:
            return t

    return -1