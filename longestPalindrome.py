
s=input()

def longestPalindrome(strs):
    #max를 취해 최장값을 걸러내야 하므로 0으로 초기값설정
    answer = 0
    for i in range(len(strs)):
        for j in range(len(strs),i,-1):
            #매 단계마다 비교, 각 단계에서 팰린드롬이냐??
            if s[i:j]==s[i:j][::-1]:    #맞다면
                answer = max(answer, j-i)
                break

    return answer

#재귀 사용예시
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))

print(longestPalindrome(s))