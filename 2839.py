import sys

N=int(input())

count=0
while N>=0:
    if N%5==0:
        count+=N//5
        print(count)
        break
    N-=3
    count+=1
else:           #else를 쓰지 않는다면 while을 정상적으로 빠져나온건지
    print(-1)   #break로 빠져나온건지 확인을 해 주어야한다
                #확인 변수를 두는것도 방법이지만 쓰지않는 변수를 줄이고 코드도 짧아지니 좋긴 함
