import sys
from collections import deque

input = sys.stdin.readline


def push_front(x):
    deq.appendleft(x)
    return

def push_back(x):
    deq.append(x)
    return

def pop_front():
    if len(deq) !=0:
        print(deq.popleft())
    else:
        print(-1)
    return

def pop_back():
    if len(deq) !=0:
        print(deq.pop())
    else:
        print(-1)
    return

def size():
    print(len(deq))
    return

def empty():
    if len(deq) != 0:
        print(0)
    else:
        print(1)
    return

def front():
    if len(deq) != 0:
        print(deq[0])
    else:
        print(-1)
    return

def back():
    if len(deq) != 0:
        print(deq[-1])
    else:
        print(-1)
    return

N= int(input())

deq = deque()

for i in range(N):
    s = input().split()
    print(s)
    if len(s) == 2:
        command = s[0]
        num = s[1]
    else:
        command = s[0]

    if command == 'push_front':
        push_front(num)
    elif command == 'push_back':
        push_back(num)
    elif command == 'pop_front':
        pop_front()
    elif command == 'pop_back':
        pop_back()
    elif command == 'size':
        size()
    elif command =='empty':
        empty()
    elif command == 'front':
        front()
    else:
        back()
