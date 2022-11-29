import sys

input = sys.stdin.readline

#이해 오래걸렸음
#예외처리가 너무 많아서 다시 짜봐야

s=list(input().strip())
tag=False
word=''
result=''
for i in s:
  #뒤집어서 출력
  if tag==False:
    if i=='<':
      tag=True
      word=word+i
    #중간점검
    elif i==' ':
      word=word+i  
      result=result+word
      word=''
    else:
      word= i + word    #들어오는문자 + 기존문자로 자동으로 뒤집어짐

  #정상적으로 출력
  elif tag==True:
    word=word+i
    if i=='>':
      tag=False
      result=result+word
      word=''

print(result+word)
