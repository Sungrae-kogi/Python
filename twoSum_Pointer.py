def twoSum_Pointer(nums, target):
    left,right = 0, len(nums)-1
    while left != right:
        if nums[left]+nums[right] > target:
            right-=1
        elif nums[left]+nums[right] < target:
            left+=1
        else:
            return left, right

#두 포인터를 이용한 풀이도 O(n)으로 빠른속도가 기대되나 index를 찾아야 하는 문제의 경우 선행 정렬이 필요하게되어 index가 꼬이는문제
#ex) def twoSum_Pointer(nums,target):
#       nums.sort()