from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

strings = defaultdict(list)

#알파벳 순으로 정렬하면 애너그램끼리는 공통된 key값을 가질 것이다.
for word in strs:
    strings["".join(sorted(word))].append(word)

print(strings)
