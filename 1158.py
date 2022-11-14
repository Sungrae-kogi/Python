import sys

input = sys.stdin.readline

N, K = map(int,input().split())

queue = [x for x in range(1,N+1)]

stack = []
idx = 0
for i in range(N):
    idx +=K-1
    if idx >= len(queue):
        idx = idx%len(queue)
    stack.append(str(queue.pop(idx)))

print("<",", ".join(stack),">", sep="")

    
        
