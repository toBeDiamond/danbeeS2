# 2075. N번째 큰 수
import sys, heapq

N = int(sys.stdin.readline())
heap = []  # 우선순위 큐
for i in range(N):
    number = list(map(int, sys.stdin.readline().split()))
    for num in number:
        if len(heap) < N:  # heap의 크기를 N으로 유지 => 원소의 개수가 N개 미만
            heapq.heappush(heap, num)  # 우선순위 큐에 push
        else:  # heap의 크기를 N으로 유지 => 원소의 개수가 N개
            if heap[0] < num:  # 현재 확인하고 있는 수가 우선순위 큐의 최소값보다 크면
                heapq.heappop(heap)  # 우선순위 큐의 최소값 제거
                heapq.heappush(heap, num)  # 현재 확인하고 있는 num을 우선순위 큐에 push
print(heap[0])
