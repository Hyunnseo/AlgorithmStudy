N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(V):
	visited1[V] = 1  #방문 처리
	print(V, end = ' ')
	for i in range(1, N+1):
		if graph[V][i] == 1 and visited1[i] == 0:    #graph상 두 정점이 연결되어있고 방문 전이라면
				dfs(i)

def bfs(V):
	queue = [V]
	visited2[V] = 1
	while queue:
		V = queue.pop(0)   #방문 노드 제거
		print(V, end = ' ')
		for i in range(1, N+1):
			if (visited2[i] == 0 and graph[V][i] == 1):
				queue.append(i)
				visited2[i] = 1 #방문 처리

dfs(V)
print()
bfs(V)
