# 1012 유기농 배추
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(i, j):
    Q = []
    visited[i][j] = 1  # 방문 체크
    Q.append((i, j))
    while Q:
        ci, cj = Q.pop()
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            if (
                (0 <= ni < N and 0 <= nj < M)
                and arr[ni][nj] == 1
                and visited[ni][nj] == 0
            ):
                Q.append((ni, nj))
                visited[ni][nj] = 1  # 방문 체크


T = int(input())
for _ in range(T):
    M, N, K = map(
        int, input().split()
    )  # M: 배추 밭의 가로 길이, N: 세로 길이, k: 배추가 심어져 있는 위치의 개수
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    print(cnt)
