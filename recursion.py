# Reverse of the number

def reversing(n,rev=0):
    if n==0:
        return rev
    return reversing(n//10,rev=rev*10+n%10)
print(reversing(12345))

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