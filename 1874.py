import sys

#1874

input = sys.stdin.readline

stack = []
result = []
switch = 0

count = 0

n = int(input())

for i in range(n):
    num = int(input())

    #num값이 될만큼 +를 stack에 input
    while count < num:
        count +=1
        stack.append(count)
        result.append('+')
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    else:
        switch=1
        break

if switch==1:
    print('NO')

for i in result:
    print(i)
