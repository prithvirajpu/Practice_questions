# move the zeros to the end
arr = [3, 4, 0, 0, 6, 0, 7, 0, 0, 8]

j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)

# find the extra value
arr1=[0,1,2,3]
arr2=[0,1,2,3,4]

res=0
for i in arr1:
    res^=i
for i in arr2:
    res^=i
    
print(res)

# remove the duplicates

arr=[1,1,2,2,3,3,4,5,6,7,7,8,8,9,9]

j=0
for i in range(1,len(arr)-1):
    if arr[i]!=arr[j]:
        j+=1
        arr[j]=arr[i]
print(arr)