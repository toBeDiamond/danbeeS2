# 4963. 섬의 개수
import sys

sys.stdin = open("input.txt")

direction = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
]  # 8방향 탐색


def bfs(i, j):
    Q = []
    visited[i][j] = 1  # 방문 체크
    Q.append((i, j))

    while Q:
        ci, cj = Q.pop()
        for di, dj in direction:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < h and 0 <= nj < w:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    Q.append((ni, nj))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 종료조건
    arr = [list(map(int, input().split())) for _ in range(h)]  # 지도
    visited = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
