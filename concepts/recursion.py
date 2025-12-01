# Anagram

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    if len(s1)==0:
        return True
    m1=min(s1)
    m2=min(s2)
    if m1!=m2:
        return False
    s1=s1.replace(m1,'')
    s2=s2.replace(m2,'')
    return anagram(s1,s2)
print(anagram('hello','oellh'))

# FInd the second largest element

arr=[1,2,3,4,5,6,7,88,44,33,56,66]
def sec_largest(arr,index=0,large=0,sec=0):
    if index==len(arr):
        return sec
    if arr[index]>large:
        sec=large
        large=arr[index]
    elif arr[index]>sec and arr[index]!=large:
        sec=arr[index]
    return sec_largest(arr,index+1,large,sec)
print(sec_largest(arr))

# Find large element
 
arr=[1,2,3,4,5,6,7,88,44,33,56,66]
def largerst_element(arr,index=0,large=0):
    if index==len(arr):
        return large
    if arr[index]>large:
        large=arr[index]
    return largerst_element(arr,index+1,large)
print(largerst_element(arr))

# Binary search

def binary_search(arr,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        return binary_search(arr,mid+1,right,target)
    else:
        return binary_search(arr,left,mid-1,target)

arr=[1,2,3,4,5,6,7,8,9]
target=8
left=0
right=len(arr)-1
print(binary_search(arr,left,right,target))

# Reverse of the number

def reversing(n,rev=0):
    if n==0:
        return rev
    return reversing(n//10,rev=rev*10+n%10)
print(reversing(12345))

# Reversing string

def string_reverse(s):
    if len(s)<=1:
        return s
    return string_reverse(s[1:])+s[0]
print(string_reverse('hello there'))

# Sum of digits

def digit_sum(n):
    if n<=1:
        return 1
    return n%10+digit_sum(n//10)
print(digit_sum(123))

# count of digits
 
def count_digit(n):
    if n==0:
        return 0
    return 1+count_digit(n//10)
print(count_digit(2234))

# First n natural numbers sum

def natural(n):
    if n==0:
        return n
    return n+natural(n-1)
print(natural(5))

# Print first 10 numbers

def ten(n,start=1):
    if start==n+1:
        return 
    print(start)
    return ten(n,start+1)
ten(10)

# Print from 10 to 1

def number(n):
    if n==0:
        return
    print(n)
    return number(n-1)
number(10)