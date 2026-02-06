from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    
    answer = 0
    while queue:
        curr = queue.popleft()
        if any(curr[1] < p[1] for p in queue):
            queue.append(curr)
        else:
            answer += 1
            
            if location == curr[0]:
                return answer