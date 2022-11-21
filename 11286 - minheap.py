import sys
import heapq

input = sys.stdin.readline
heap = []

N=int(input())

#연산에 대한 정보를 나타내는 정수 x가 입력
#** 힙 요소는 튜플일 수 있다. 기준이 될 레코드와 값을 지정
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap,[abs(x),x])
    else:
        if not heap:
            print(0)
        else:
            #배열에서 절댓값이 가장 작은 값을 출력 절댓값기준 min heap 구현되어있으니
            #가장 작은 값을 출력하고 배열에서 제거
            print(heapq.heappop(heap)[1])
    
