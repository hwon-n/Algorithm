def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i > budget:
            return answer
        else:
            budget -= i
            answer += 1
    return answer