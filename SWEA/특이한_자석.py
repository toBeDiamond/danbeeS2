# 4013. [모의 SW 역량테스트] 특이한 자석
from collections import deque


def dfs(num, dir):
    flag[num] = 1  # 방문 체크
    if num < 3:  # 왼쪽 접촉면 확인
        if magnet[num][2] != magnet[num + 1][6] and flag[num + 1] == 0:
            dfs(num + 1, dir * -1)
    if num > 0:  # 오른쪽 접촉면 확인
        if magnet[num][6] != magnet[num - 1][2] and flag[num - 1] == 0:
            dfs(num - 1, dir * -1)

    magnet[num].rotate(dir)  # 회전


T = int(input())
for tc in range(1, T + 1):
    turn = int(input())  # 회전 횟수
    magnet = [deque(map(int, input().split())) for _ in range(4)]  # 4개의 자석(deque으로 받기)

    for i in range(turn):
        n, d = map(int, input().split())  # 자석 번호, 회전 방향
        flag = [0, 0, 0, 0]  # 해당 자석이 회전했는지 저장
        dfs(n - 1, d)

    res = 0
    for i in range(4):
        res += magnet[i][0] * (2**i)

    print(f"#{tc} {res}")

"""
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
"""
