import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = arr[b][a] = 1


print(arr)
visited = [0] * (N+1)


def bfs(V):
    num = 0
    queue = [V]
    visited[V] = 1 #방문처리
   
    while queue:
        V = queue.pop(0)
        
        for i in range(1, N+1):
            if (visited[i] == 0 and arr[V][i] == 1):
                queue.append(i)
                visited[i] = 1
                num += 1

    print(num)



bfs(1)
