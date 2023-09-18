# 14888. 연산자 끼워넣기
N = int(input())
numbers = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())

# 최대값, 최소값 초기화
max_v = -int(1e9)
min_v = int(1e9)


def dfs(i, num):
    global max_v, min_v, plus, sub, mul, div
    if i == N:
        max_v = max(max_v, num)
        min_v = min(min_v, num)
    else:
        if plus:
            plus -= 1
            dfs(i + 1, num + numbers[i])
            plus += 1  # 초기화 (제자리에 돌려 놓기)
        if sub:
            sub -= 1
            dfs(i + 1, num - numbers[i])
            sub += 1  # 초기화 (제자리에 돌려 놓기)
        if mul:
            mul -= 1
            dfs(i + 1, num * numbers[i])
            mul += 1  # 초기화 (제자리에 돌려 놓기)
        if div:
            div -= 1
            dfs(i + 1, int(num / numbers[i]))
            div += 1  # 초기화 (제자리에 돌려 놓기)


dfs(1, numbers[0])
print(max_v)
print(min_v)
