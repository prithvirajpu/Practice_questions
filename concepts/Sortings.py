# Bubble Sorting

arr=[3,4,2,5,6,77,4,55,12]
for i in range(len(arr)-1):
    flag=0
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=1
    if flag==0:
        break
print(arr)

# Selection Sorting

arr=[3,4,2,5,6,77,4,55,12]
for i in range(len(arr)-1):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    if mini!=i:
        arr[i],arr[mini]=arr[mini],arr[i]
print(arr)

# Insertion sorting

arr=[3,2,5,6,77,4,55,12]
for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    while j>=0 and temp<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print(arr)

# Merge sorting

# Efficient one because of the index calls

def merge_sort(arr, s, e):
    if e - s <= 1:
        return
    mid = (s + e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid, e)
    merge(arr, s, mid, e)

def merge(arr, s, m, e):
    mix = []
    i, j = s, m
    while i < m and j < e:
        if arr[i] < arr[j]:
            mix.append(arr[i])
            i += 1
        else:
            mix.append(arr[j])
            j += 1
    if i < m:
        mix.extend(arr[i:m])
    if j < e:
        mix.extend(arr[j:e])
    for k in range(len(mix)):
        arr[s + k] = mix[k]
        
arr = [5, 2, 9, 1, 6, 3]
merge_sort(arr, 0, len(arr))
print(arr)

# Less efficient because of the slicing 

arr=[3,2,5,6,77,4,55,12]
def merge_sorting(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sorting(arr[:mid])
    right=merge_sorting(arr[mid:])
    return merging(left,right)
def merging(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
        else:
            result.append(left[i])
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge_sorting(arr))



# Quick sort

def quick_sort(nums, low, high):
    if low >= high:
        return
    s = low
    e = high
    mid = (s + e) // 2
    pivot = nums[mid]
    while s <= e:
        while nums[s] < pivot:
            s += 1
        while nums[e] > pivot:
            e -= 1
        if s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
    quick_sort(nums, low, e)
    quick_sort(nums, s, high)
    
arr = [5, 4, 33, 454, 54, 65]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
