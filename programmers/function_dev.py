# 테스트 6, 11만 통과.. 
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

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    cnt = 0
    time = 0
    while progresses:
        if progresses[0] + speeds[0] * time >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
            
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
        
    answer.append(cnt)
    return answer