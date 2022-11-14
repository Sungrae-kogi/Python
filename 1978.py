N=int(input())

a=list(map(int, input().split()))

count=0
for i in a:
    bo=0
    if(i==1):
        continue
    for j in range(2,i):    #2부터 자기자신직전까지
        if(i%j==0):
            bo=1
    if bo==0:
        count+=1

print(count)
