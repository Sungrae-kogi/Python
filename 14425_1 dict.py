import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = {}
for i in range(N):
    S[input().strip()]=1

arrays = []
for i in range(M):
    s = input().strip()
    if s not in S:
        S[s] = 0
    arrays.append(s)
    
count = 0
for i in arrays:
    if S[i]==1:
        count+=1

print(count)
