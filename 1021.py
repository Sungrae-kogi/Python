import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

deq = deque([x for x in range(1,N+1)])
#1,2,3,4,5,6...

s = list(map(int,input().split()))

count = 0


def left():
    global count
    deq.append(deq.popleft())
    count+=1

def right():
    global count
    deq.appendleft(deq.pop())
    count+=1


#M번
for i in range(M):
    q_len = len(deq)
    q_idx = deq.index(s[i]) #찾아야할 idx
    if q_idx <= len(deq)//2:
        #왼쪽에 가깝다면
        while True:
            if deq[0] == s[i]:
                deq.popleft()
                break
            else:
                left()
    else:
        #오른쪽에 가깝다면
        while True:
            if deq[0] == s[i]:
                deq.popleft()
                break
            else:
                right()

print(count)
