def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        
        res = array[i:j]
        res.sort()
        answer.append(res[k])
    return answer