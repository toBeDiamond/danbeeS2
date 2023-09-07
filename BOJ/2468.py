# 2468 안전 영역
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(i, j, num):
    Q = []
    visited[i][j] = 1
    Q.append((i, j))

    while Q:
        ci, cj = Q.pop()  # 현재 인덱스
        for di, dj in direction:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] > num and not visited[ni][nj]:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
min_h = 101
for item in arr:
    if max(item) > max_h:
        max_h = max(item)
    if min(item) < min_h:
        min_h = min(item)

res = 0
for rain in range(min_h-1, max_h+1):  # rain: 비의 양
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and not visited[i][j]:  # 비의 양보다 높고 방문하지 않았으면
                cnt += 1
                bfs(i, j, rain)
    res = max(res, cnt)

print(res)