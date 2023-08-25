# 1258. 행렬찾기
def find_start(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:  # 빈 용기가 아니고
                # 직사각형 사이에 0 원소들(빈 용기들)이 있음 => 시작점이 배열의 경계이거나 윗줄이나 왼쪽줄이 0이면 시작 인덱스
                if (arr[i][j - 1] == 0 or j == 0) and (arr[i - 1][j] == 0 or i == 0):  #
                    start.append([i, j])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = []
    find_start(arr, N)

    size = []
    for r, c in start:
        width = 0
        height = 0
        while arr[r][c] != 0:
            width += 1
            c += 1  # 한칸 옆으로 이동
            if c > N - 1:
                break  # 유효한 인덱스를 넘어가면 반복문 종료

        c -= width  # while문을 돌면서 c를 증가시켰기 때문에 초기화

        while arr[r][c] != 0:
            height += 1
            r += 1  # 한칸 옆으로 이동
            if r > N - 1:
                break  # 유효한 인덱스를 넘어가면 반복문 종료

        mul = width * height
        size.append((mul, height, width))

    size.sort()  # mul 기준으로 정렬

    result = []
    for mul, row, col in size:
        result.append(row)
        result.append(col)

    cnt = len(size)
    print(f"#{tc} {cnt}", *result)
