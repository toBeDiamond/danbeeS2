# 13305. 주유소
N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_v = price[0]
for i in range(N - 1):  # 마지막 주유소에서 기름을 구입할 필요가 없으므로 제외
    if min_v > price[i]:
        min_v = price[i]

    result += min_v * road[i]

print(result)
