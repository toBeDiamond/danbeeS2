# 2644.  촌수계산
def dfs(v, cnt):
    visited[v] = 1  # 방문체크

    if v == e:
        result.append(cnt)
        return

    for w in range(1, N + 1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w, cnt + 1)


N = int(input())
s, e = map(int, input().split())

adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

m = int(input())
result = []

for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

dfs(s, 0)
if result:
    print(result[0])
else:
    print(-1)
