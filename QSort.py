array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:    #원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        #pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:  #끝에 도달하지않았고 pivot값보다 작다면
            left += 1
        #pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:    #만일 교차되었다면 작은데이터와 피봇을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   #교차된게 않았으면 작은데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    #분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


#일반적인경우 시간복잡도가 O(NlogN)이지만 최악의 경우 O(N^2)
            
