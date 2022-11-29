import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    dict = {}
    for j in range(n):
        name, type = input().split()
        if type in dict:
            dict[type].append(name)
        else:
            dict[type] = [name]
        
    num = 1
    for key in dict:
        num *= len(dict[key])+1

    print(num-1)
