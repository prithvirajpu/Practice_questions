# person with max score

scores = {"Alice": 450, "Bob": 780, "Charlie": 620, "Diana": 710}
res=max(scores,key=scores.get)
print(res)

# Problem: You have a list of student records where each tuple contains (Name, Grade, Age).
#  Sort the list primarily by Grade (descending), and if grades are equal, secondarily by Age (ascending).
students = [("Alice", 85, 20), ("Bob", 95, 19), ("Charlie", 85, 18), ("Diana", 95, 21)]

res=sorted(students,key=lambda x: (-x[1],x[2]))
print(res)

# Sort by the second element (the words)

pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda item: item[1])

print(sorted_pairs)

# sort by price
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200},
    {"name": "Keyboard", "price": 75}
]
res=sorted(products,key=lambda x: x['price'],reverse=True)
print(res)

# Find subarrays which give a target sum
arr=[1,2,3,4,5,6,7]
target=6
for i in range(len(arr)):
    curr_sum=0
    for j in range(i,len(arr)):
        curr_sum+=arr[j]
        if curr_sum==target:
            print((arr[i:j+1]))

# Smallest and largest

arr=[3,4,5,2,1,33,66,22,123,43,47,24]
small=arr[0]
large=arr[0]
for i in arr:
    if i<small:
        small=i
    if i>large:
        large=i
print(small)
print(large)

# large, second large and third large
arr=[11,44,22,88,33,99,55,77]

large=0
sec=0
third=0
for i in arr:
    if i>large:
        third=sec
        sec=large
        large=i
    elif i>sec and i !=large:
        third=sec
        sec=i
    elif i>third and i!=large and i !=sec:
        third=i
print(large)
print(sec)
print(third)

# reverse the array
arr=[11,44,22,88,33,99,55,77]

j=len(arr)-1
i=0
while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(f'reversed array is {arr}')

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

# two sum 
arr=[10,24,6,14,4]
new={}
target=28

for i in range(len(arr)):
    balance=target-arr[i]
    if balance in new:
        print(f'the Indices are: {new[balance]},{i}')
        break
    new[arr[i]]=i

