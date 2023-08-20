# 2527. 직사각형
T = 4
for _ in range(T):
    w1, h1, w2, h2, w3, h3, w4, h4 = map(int, input().split())
    # 공통 부분이 없음
    if (w4 < w1) or (w2 < w3) or (h2 < h3) or (h4 < h1):
        print("d")
    # 점
    elif (
        (w1 == w4 and h1 == h4)
        or (w2 == w3 and h1 == h4)
        or (w2 == w3 and h2 == h3)
        or (w1 == w4 and h2 == h3)
    ):
        print("c")
    # 선분
    elif (h1 == h4) or (h2 == h3) or (w1 == w4) or (w2 == w3):
        print("b")
    # 직사각형
    else:
        print("a")
