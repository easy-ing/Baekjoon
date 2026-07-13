def solution(nums):
    kinds = set(nums)
    can_select = len(nums) // 2

    if len(kinds) < can_select:
        return len(kinds)

    return can_select