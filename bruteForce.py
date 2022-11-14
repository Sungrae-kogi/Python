#bruteForce twoSum
def twoSum(nums, target):
    for i in range(len(nums)):
        #i의 바로 앞에서 끝까지 전부순회
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]


#풀이복잡도 O(n^2) -> 최적화
#dict를 이용한 O(1)~ O(n)
def twoSum_dict(nums, target):
    nums_dict = {}
    for i,num in enumerate(nums):
        #target-현재수 가 존재하고 ** 같은 두 수를 가리키는게 아닐때, ex) 6= 3+3
        if target-num in nums_dict:
            return [nums_dict[target-num], i]
        nums_dict[num] = i

nums = [3,3,11,15]
target= 6
print(twoSum_dict(nums,target))