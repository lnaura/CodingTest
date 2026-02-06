from collections import deque
def solution(n, computers):
    
    visited = [False] * n
    
    def bfs(start_node):
        queue = deque([start_node])
        visited[start_node] = True
        
        while queue:
            curr = queue.popleft()
            for neighbor in range(n):
                if not visited[neighbor] and computers[curr][neighbor] == 1:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    answer = 0
    for i in range(n):
            if not visited[i]:
                bfs(i)
                answer += 1
    return answer