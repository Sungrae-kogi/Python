#a층의 b호에 살려면 자신의 아래 (a-1)층의 1호부터 b호까지의 사람수를 데리고 들와야 살 수 있다.
T = int(input())

#k층의 n호
def people(k,n):
    number = 0
    if k==0:    #0층이면 사람은 호인 n명이 산다
        return n
    else:
        for i in range(1,n+1):
            number = number + people(k-1,i)
        return number


for i in range(T):
    k = int(input())
    n = int(input())

    print(people(k,n))
