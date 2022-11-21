import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set([input() for _ in range(N)])

count = 0
for i in range(M):
    s = input()
    if s in S:
        count+=1

print(count)
