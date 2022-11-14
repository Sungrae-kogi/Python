import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque(range(1,N+1))


while len(queue) !=1:
    queue.popleft() #맨 위의카드 하나를 버림
    pick = queue.popleft() #맨 위의 카드를 빼서 맨밑으로
    queue.append(pick)

print(queue[0])
