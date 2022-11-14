#numRows 행에 따라 지그재그로 배열하여 결과문자열 리턴
def solution(s, numRows):
    #exception
    if numRows==1:
        return s
    store = [[] for _ in range(numRows)]
    ans = ''

    #첫행 0부터 numRows-1까지
    i=0
    #True면 i+=1
    flag=True
    for x in s:
        store[i].append(x)
        #끝행이아니면 flag True유지
        if i==0:
            flag = True
        elif i==numRows-1:
            flag  = False
        if flag:    #True아직 끝행이아니라 내려가고있는중이면
            i+=1    #내려감
        else:
            i-=1
    for i in range(numRows):
        ans += ''.join(store[i])

    return ans

s = input()
numRows = int(input())
print(solution(s,numRows))