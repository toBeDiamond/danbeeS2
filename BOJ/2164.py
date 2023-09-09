# 2164. 카드2
from collections import deque

N = int(input())
cards = deque([i for i in range(1, N + 1)])

# 카드 놀이 규칙
# 1. 제일 위의 카드를 버린다.
# 2. 그 다음 제일 위의 카드를 맨 밑에 넣는다.
# 3. 카드 1장이 남을 때까지 반복한다.

res = 0
while cards:
    res = cards.popleft()
    if cards:
        tmp = cards.popleft()
        cards.append(tmp)

print(res)
