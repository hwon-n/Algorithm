def solution(nums):
    n = int(len(nums)/2)
    poketmon = []
    for num in nums:
        if len(poketmon) == n:
            return len(set(poketmon))
        if num not in poketmon:
            poketmon.append(num)
    return len(set(poketmon))