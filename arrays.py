# Deleting item from certain position

arr=[1,2,3,4,5]
index=2
n=len(arr)-1
for i in range(index-1,n):
    arr[i]=arr[i+1]
arr.pop()
print(arr)

# Inserting value at specific position

arr=[1,2,3,4,5]
index=1
val=99
arr.append(0)
n=len(arr)-1
for i in range(n,index,-1):
    arr[i]=arr[i-1]
arr[index]=val
print(arr)

# duplicate removing

arr = [1,2,3,4,2,3,4,2,3,4,4,45,56,4,5,5,5,5,5,5,54,4]
n=len(arr)
i=0
while i<n:
    j=i+1
    while j<n:
        if arr[i]==arr[j]:
            k=j
            while k<n-1:
                arr[k]=arr[k+1]
                k+=1
            n-=1
        else:
            j+=1
    i+=1

del arr[n:]
print(arr)