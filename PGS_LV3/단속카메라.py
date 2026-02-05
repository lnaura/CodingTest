def solution(routes):
    routes.sort(key = lambda x : x[1])
    last_camera = -30001
    answer = 0
    
    for start, end in routes:
        if last_camera < start:
            last_camera = end
            answer += 1
            
    return answer