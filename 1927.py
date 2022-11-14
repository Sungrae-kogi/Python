import sys, heapq

input = sys.stdin.readline

N=int(input())

heap = []

for i in range(N):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            res = heapq.heappop(heap)
            print(res)
    else:
        heapq.heappush(heap,num)
