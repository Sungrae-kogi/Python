from collections import deque


def isPalindrome(self, s: str) -> bool: #함수의 리턴타입 명시
    strs =[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():   #리스트의 pop(0)는 O(n)이다
            return False

    return True


#deque 자료형 사용법 -> 좀더 속도향상 가능 deque의 popleft()는 같은기능이지만 O(1)이기 때문
def isPalindrome(self, s: str) -> bool:
    #deque선언
    strs = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True