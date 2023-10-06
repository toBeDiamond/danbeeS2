# 4012. [모의 SW 역량테스트] 요리사
import sys

sys.stdin = open("요리사_input.txt")


def solve(A, B):
    sum_a = sum_b = 0
    for i in range(M):
        for j in range(i + 1, M):
            sum_a += arr[A[i]][A[j]] + arr[A[j]][A[i]]
            sum_b += arr[B[i]][B[j]] + arr[B[j]][B[i]]
    return abs(sum_a - sum_b)


def dfs(n, k):
    global min_v
    if n > M:
        return

    if n == M:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        res = solve(A, B)
        min_v = min(res, min_v)
        return

    for i in range(k, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n + 1, i + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_v = 987654321
    dfs(0, 0)

    print(f"#{tc} {min_v}")
