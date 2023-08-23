import sys
sys.setrecursionlimit(1000000)
#재귀를 사용해서 풀어야 하는 문제라면, 위 코드 사용이 필수
#파이썬 기본 재귀 깊이 제한은 1000으로 매우 얕아서, 재귀로 문제 풀 경우 이 제한 걸릴 수 있음

n = int(input())

arr = [[ 0 for col in range(n)] for row in range(n)]
visited = [[False for row in range(n)] for col in range(n)]

sum1 = 0
sum2 = 0
#정상인과 색약인 사람의 경우를 저장할 변수 선언

for i in range(n):
    arr[i] = list(sys.stdin.readline().rstrip())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
#인접한 칸의 상하좌우로 이동하기 때문에 행, 열 리스트를 각각 만들어서 정의 ->  for문으로 쉽게 풀려고 생성하는 것

#얘는 위아래, 양 옆 케이스로 나누어진게 아니라 동서남북을 다 탐색해야 한다.
def dfs(x,y, color):
    #방문하면 True로 값 바꿔줌
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #인덱스 범위 내에 있고, 방문한 적이 없다면 조건문 실행
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0:
            if arr[nx][ny] == color:
                dfs(nx, ny, color)


#빨 초 파 순서대로 확인
for color in ['R', 'G', 'B']:
    for i in range(n):
        for j in range(n):
            #방문한 적이 없고 R,G,B 중에 있다면 dfs 실행
            if visited[i][j] == 0 and arr[i][j] == color:
                dfs(i, j, color)
                sum1 += 1

#G를 R로 바꾸는 반복문
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'



#한번 더 실행할거니까 visited 배열 다시 초기화
visited = [[False for row in range(n)] for col in range(n)]
for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            #방문한 적이 없고 R, B 중에 있다면 dfs 실행
            if visited[i][j] == 0 and arr[i][j] == color:
                dfs(i, j, color)
                sum2 += 1


print(sum1, sum2)
