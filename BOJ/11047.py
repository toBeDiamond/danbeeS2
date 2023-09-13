# 11047. 동전0
# 입력
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
money = [int(input().strip()) for _ in range(N)]
money.sort(reverse=True)

# 로직
cnt = 0
for m in money:
    cnt += K // m
    K = K % m

# 출력
print(cnt)
