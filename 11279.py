import heapq, sys

input = sys.stdin.readline

#heapq에서는 최대 힙을 제공 x 따라서 -로 입력받고 출력할때 다시 -붙이는식으로
#최대 힙 구현

N = int(input())

heap = []

for i in range(N):
    num = int(input())
    if num == 0:
        if len(heap) ==0:
            print(0)
        else:
            #-로 들어가있을 가장 작은값(가장절댓값이큰)을 다시 음수붙여서 꺼냄 == 최대힙
            res = -heapq.heappop(heap)
            print(res)
    else:
        #최대 힙 구현을 위한 트릭으로 값들을 음수로 넣음
        heapq.heappush(heap,-num)
