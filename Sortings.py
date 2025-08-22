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
