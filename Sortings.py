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
