import sys

input = sys.stdin.readline

img = input().strip()

#'('가 올 때는 stack에 
stack =[]
count=0

for i in range(len(img)):
    if img[i]=='(':
        stack.append(img[i])
    else:   #')'가 오면 case 2가지로 구분
        #괄호를 닫게되니 stack.pop하고 len(stack)만큼 count에 더함
        if img[i-1]=='(':
            stack.pop()
            count += len(stack)
        #이전에온게 ')'라면 막대 하나가 끝난거니 count +1
        else:
            stack.pop()
            count += 1


print(count)
    
