from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    answer = 0

    # gcdA가 arrayB의 어떤 원소도 나누지 못하는 경우
    if all(b % gcdA != 0 for b in arrayB):
        answer = max(answer, gcdA)

    # gcdB가 arrayA의 어떤 원소도 나누지 못하는 경우
    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)

    return answer