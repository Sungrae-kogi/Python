import sys

input = sys.stdin.readline

N, K= map(int, input().split())

queue = [x for x in range(1,N+1)]

stack =[]
idx = 0

#일부 한글 깨
#N개의 리스트가 다 사라질때까지 반복
for i in range(N):
    idx += K-1
    if idx >= len(queue):
        idx %=len(queue)
    stack.append(str(queue.pop(idx)))

print("<", ", ".join(stack),">", sep="")
