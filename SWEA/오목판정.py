# 11315. 오목 판정 - D3
import sys

sys.stdin = open("input.txt")

direction = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]


def judge_five(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                for di, dj in direction:  # 8방향 탐색
                    cnt = 1
                    for k in range(1, 5):
                        ni = i + di * k
                        nj = j + dj * k
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == "o":
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        return "YES"
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    print(f"#{tc} {judge_five(board, N)}")
