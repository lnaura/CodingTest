import math

def solution(progresses, speeds):
    n = len(progresses)
    
    days = []
    for i in range(n):
        d = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(d)
    
    answer = []
    prev_d = days[0]
    cnt = 0
    for day in days:
        if day > prev_d:
            answer.append(cnt)
            cnt = 1 
            prev_d = day
        else:
            cnt += 1
            
    if cnt > 0:
        answer.append(cnt)
    
    return answer