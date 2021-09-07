def main():
    
    make_file(n)
    pascal(n)
    for i in a:
        print(i)


#입력받은 n단 만큼의 행렬을 0의 값으로 채워 만들어 놓음
def make_file(n):
    for i in range(n):
        b=[]
        for j in range(i+1):
            b.append(0)

        a.append(b)
    print("삼각형이 들어갈 행렬의 뼈대가완성")


#i행과 j열에 알맞은 파스칼의 삼각형 값을 넣음
def pascal(n):
    for i in range(n):
        for j in range(i+1):
        
            if i==0 or j==0:
                a[i][j]=1
            elif i==j:
                a[i][j]=1
            else:
                a[i][j]=a[i-1][j-1]+a[i-1][j]


#만들고자 하는 파스칼의 삼각형 단 수 n 입력
print("만들고자 하는 삼각형의 단 수 n 입력")
n=int(input())
print("n=",n)
a=[]



print("main함수 실행")        
main()
