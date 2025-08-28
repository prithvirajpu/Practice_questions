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
