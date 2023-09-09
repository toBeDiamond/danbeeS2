# 11286. 절댓값 힙
import sys, heapq

abs_heap = []  # 절대값 힙
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:  # x가 0이 아니면
        heapq.heappush(abs_heap, (abs(x), x))
    else:  # x가 0이고
        if abs_heap:  # abs_heap이 비어 있지 않으면
            print(heapq.heappop(abs_heap)[1])  # 절대값이 가장 작은 값 삭제 + 출력
        else:  # abs_heap이 비어 있으면
            print(0)
