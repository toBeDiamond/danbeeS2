# 8979. 올림픽
N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # 금메달, 은메달, 동메달 순으로 내림차순 정렬

# K국가의 인덱스 찾기
for i in range(N):
    if medals[i][0] == K:
        idx = i

# 동점 국가 찾기
for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(idx+1)
        break