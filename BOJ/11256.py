# 11256. 사탕
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    candy, N = map(int, input().split())

    box_size = []
    for n in range(N):
        r, c = map(int, input().split())
        box_size.append(r * c)

    box_size.sort(reverse=True)  # 상자 크기를 내림차순으로 정렬
    cnt = 0

    for box in box_size:
        if candy <= 0:
            break
        candy -= box
        cnt += 1
    print(cnt)
