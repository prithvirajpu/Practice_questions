# sort until the k index

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

# Merging two sorted arrays using the merge sort
arr1=[4,5,6,7]
arr2=[1,2,3]

def merge(arr1,arr2):
    result=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    if i<len(arr1):
        result.extend(arr1[i:len(arr1)])
    if j<len(arr2):
        result.extend(arr2[j:len(arr2)])
    arr1[:]=result
merge(arr1,arr2)
print(arr1)
