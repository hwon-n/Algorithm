def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            res = numbers[i] + numbers[j]
            answer.add(res)
    
    answer = list(answer)
    return answer