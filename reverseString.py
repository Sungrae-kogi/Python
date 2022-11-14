import sys

#1. 로그의 맨 앞부분은 식별자
#2. 문자로 구성된 로그가 숫자 로그보다 앞에
#3. 문자가 동일한 경우 식별자 순으로
#4. 숫자 로그는 입력 순서대로  -> 정렬 따로 필요x
from typing import List


def sortLog(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #2개의 키를 람다 표현식으로 정렬
    #식별자를 제외한 문자열 [1:]을 기준으로 정렬하되, 동일한 경우 후순위로 식별자 [0]를 지정해 정렬되도록
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

log = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = sortLog(log)
print(result)

