# 14889. 스타트와 링크
def cal(a, b):
    a_scr = b_scr = 0
    for i in range(M):
        for j in range(M):
            a_scr += arr[a[i]][a[j]]
            b_scr += arr[b[i]][b[j]]
    return abs(a_scr - b_scr)


def dfs(n, A, B):
    global min_v

    if min_v == 0:  # 가지치기
        return

    if n == N:
        if len(A) == len(B):  # 같은 인원수로 팀이 구성되면
            print(A, B)
            min_v = min(min_v, cal(A, B))
        return

    dfs(n + 1, A + [n], B)  # A팀 선택
    dfs(n + 1, A, B + [n])  # B팀 선택


N = int(input())
M = N // 2
arr = [list(map(int, input().split())) for _ in range(N)]

min_v = 987654321
dfs(0, [], [])

print(min_v)
