from collections import deque

import sys
N, M = map(int, sys.stdin.readline().split())

arr = [[0]*M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int,sys.stdin.readline().rstrip()))



visited = [[0]*M for _ in range(N)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q= deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= N or ny<0 or ny>=M:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

    return arr[N-1][M-1]

print(bfs(0,0))
                
