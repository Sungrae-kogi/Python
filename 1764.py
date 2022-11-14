import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
see = set()


for i in range(N):
    listen.add(input().strip())

for i in range(M):
    see.add(input().strip())


#집합 set()에서 교집합은 & 합집합은 | 차집합은 -임을 활용한 풀이 
print(len(listen&see))
for i in sorted(listen&see):
    print(i)
