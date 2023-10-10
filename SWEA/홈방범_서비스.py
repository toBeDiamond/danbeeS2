# 2117. [모의 SW 역량테스트] 홈 방범 서비스
from collections import deque


def bfs(ci, cj, k):
    global res
    visited = [[0] * N for _ in range(N)]
    Q = deque([(ci, cj)])
    visited[ci][cj] = 1
    cnt = arr[i][j]

    for _ in range(k - 1):
        for _ in range(len(Q)):
            ci, cj = Q.popleft()
            for di, dj in direction:
                ni = ci + di
                nj = cj + dj
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    Q.append((ni, nj))
                    if arr[ni][nj] == 1:
                        cnt += 1

    cost = (k * k) + (k - 1) * (k - 1)

    if cost <= M * cnt:
        res = max(res, cnt)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 도시의 크기, M: 하나의 집이 지불할 수 있는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]  # 도시의 정보
    direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
    res = 0

    for i in range(N):
        for j in range(N):
            for k in range(N * 2):
                bfs(i, j, k)

    print(f"#{tc} {res}")
