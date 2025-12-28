# monkey patching-runtime modifying the methods functions 
class Person:
    def greet(self):
        return 'hello'
def new_greet(self):
    return 'new_greet'
Person.greet=new_greet
p=Person()
print(p.greet())

# creating decorator for finding the time
import time
def outer(fn):
    def inner(x):
        start=time.time()
        fn(x)
        end=time.time()
        print(f'time taken {end-start:.2f}')
    return inner
@outer
def fn(x):
    res=[]
    for i in range(x):
        res.append(i**2)
    return res
fn(1000000)

# Generator function 
# printing odd numbers
def odd_number():
    i=0
    while True:
        if i%2!=0:
            yield i
        i+=1
x=odd_number()
print(next(x))
print(next(x)) # print(x.__next__())

# Decorator
def outer(fn):
    def inner(a,b):
        print('start')
        fn(a,b)
        print('end')
    return inner
@outer
def deco(a,b):
    print(a+b)
deco(10,20)

# shallow copy -outer side copy and inner is reference 
import copy
arr=[1,2,[10,20]]
res=copy.copy(arr)

# res[2][0]=99
# print(res)
# print(arr)

deep=copy.deepcopy(arr)
deep[2][0]=99
print(arr)
print(deep)

# clossure
def outer(*num):
    def inner():
        print(sum(num))
    return inner
x=outer(1,2,3,4,5,6)
x()

# currying

def fn1(a):
    def fn2(b):
        def fn3(c):
            return a+b+c
        return fn3
    return fn2
x=fn1(10)
y=x(20)
print(y(20))

import os
print(os.getenv('secret_key'))

# Assert
def fn(a):
    assert a<0,'it is greater'
# fn(10)