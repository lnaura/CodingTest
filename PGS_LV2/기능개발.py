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

#----------------------------------------
import math

def solution(progresses, speeds):
    max_curr_day = math.ceil((100 - progresses[0]) / speeds[0])
    
    answer = []
    count = 0
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        
        if day > max_curr_day:
            answer.append(count)
            count = 1
            max_curr_day = day
        else:
            count += 1
    
    answer.append(count)
    
    return answer