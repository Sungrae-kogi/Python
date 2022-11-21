import sys

input = sys.stdin.readline

#탐색에 시간이 걸리니
#값을 정렬한 뒤에 이분탐색(Binary Search)로 탐색
#요소들을 확인하는 문제는 이진탐색이라고 생각하면 좋다.
#요소가 작지않은이상 순차탐색은 시간초과

def BSearch(n):
    left = 0
    right = len(num)-1
    while left <=right:
        mid = (left+right)//2
        if num[mid] == n:
            a.append(1)
            break
        elif num[mid] > n:
            right = mid-1
        else:
            left = mid+1
    else:
        a.append(0)

N = int(input())
num = list(map(int,input().split()))

M = int(input())
result= list(map(int,input().split()))
num.sort()

a = []

for i in range(len(result)):
    BSearch(result[i])
    

for i in a:
    print(i, end=' ')
    
