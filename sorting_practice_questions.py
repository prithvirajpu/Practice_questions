# sort untile the k the index

arr=[5,4,3,2,1]
k=3
for i in range(k):
    for j in range(k-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# Find the kth largest element

k=2
for i in range(k):
    flag=0
    for j in range(k-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=1
    if flag==0:
        break
print(arr[-k])

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