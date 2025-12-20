import heapq
import sys
input = sys.stdin.readline

def solve():
    
    t = int(input())
    for _ in range(t):
        max_heap = []
        min_heap = []
        k = int(input())
        visited = [False] * k
        for i in range(k):
            command , n = input().split()
            n = int(n)
            if command == 'I':
                heapq.heappush(min_heap,(n,i))
                heapq.heappush(max_heap,(-n,i))
                visited[i] = True

            elif command == 'D':
                if n == 1:
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                else:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)    

        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            # max_heap에는 음수가 들어있으므로 -를 붙여 출력
            print(-max_heap[0][0], min_heap[0][0])

solve()