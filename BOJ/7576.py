# 7576.토마토
from collections import deque


def bfs():
    Q = deque()
    # 초기 데이터 삽입
    green_tomato = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:  # 안 익은 토마토
                green_tomato += 1
            elif arr[i][j] == 1:  # 익은 토마토
                Q.append((i, j))
                visited[i][j] = 1

    while Q:
        ci, cj = Q.popleft()
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            # 유효한 범위 + 미방문 + 안 익은 토마토
            if (
                (0 <= ni < N and 0 <= nj < M)
                and visited[ni][nj] == 0
                and arr[ni][nj] == 0
            ):
                visited[ni][nj] = visited[ci][cj] + 1
                Q.append((ni, nj))
                green_tomato -= 1  # 인접한 토마토가 하나 익음

    if green_tomato:  # 안 익은 토마토가 하나라도 남아있으면
        return -1
    else:  # 토마토가 모두 익었으면
        return visited[ci][cj] - 1  # 마지막으로 방문한 곳 - 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 왼쪽, 오른쪽, 위, 아래

print(bfs())
