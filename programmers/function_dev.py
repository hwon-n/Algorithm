def solution(progresses, speeds):
    answer = []
    
    cnt = 0
    days = 1
    
    while progresses:
        progresses[0] += days * speeds[0]
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            days += 1
        
    answer.append(cnt)
    return answer