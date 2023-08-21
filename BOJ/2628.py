# 2628. 종이 자르기
w, h = map(int, input().split())
N = int(input())
width = [0, w]
height = [0, h]
for _ in range(N):
    cut, num = map(int, input().split())
    if cut: # 1은 세로로 자르기
        width.append(num)
    else:   # 0은 가로로 자르기
        height.append(num)

width.sort()
height.sort()

res = 0
for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i+1] - width[i]
        y = height[j+1] - height[j]
        res = max(res, x*y)

print(res)