# 13300. 방 배정
import math

N, maximum = map(int, input().split())
arr = [[0, 0] for _ in range(6)]
for _ in range(N):
    gen, grade = map(int, input().split())
    arr[grade - 1][gen] += 1

cnt = 0
for w, m in arr:
    cnt += math.ceil(w / maximum) + math.ceil(m / maximum)
print(cnt)
