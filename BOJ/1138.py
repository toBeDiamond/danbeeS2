# 1138. 한 줄로 서기
N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i] == cnt and result[j] == 0:
            result[j] = i + 1
            break
        if result[j] == 0:
            cnt += 1

print(*result)

## 방법 2
# N = int(input())
# arr = reversed(list(map(int,input().split())))
# result = []
# for idx in arr:
#     result.insert(idx, N)
#     N -= 1
# print(*result)
#
# # 방법 3
# N = int(input())
# arr = reversed(list(map(int,input().split())))
# result = []
# for i, val in enumerate(arr):
#     result.insert(val, N-i)
# print(*result)
