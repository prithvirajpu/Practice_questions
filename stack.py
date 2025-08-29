# stack with List

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        return self.stack.append(data)
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def print(self):
        if self.is_empty():
            print('stack is empty')
        else:
            for i in self.stack:
                print(i)
x=Stack()
x.push(10)
x.push(20)
x.push(30)
print(x.peek())
x.print()

# stack using Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        self.top=self.top.next
    def peek(self):
        return self.top.data
    def print(self):
        if self.top is None:
            return 'underflow'
        current=self.top
        while current:
            print(current.data)
            current=current.next
x=LinkedList()
x.push(10)
x.push(20)
x.push(30)
x.pop()
print(x.peek())
x.print()

# Reverse a string using stack

def reverse_string(s):
    result=[]
    for i in s.split():
        result.append(i)
    new=[]
    while result:
        new.append(result.pop())
    return new
print(" ".join(reverse_string('hello there iam here')))

# Valid parantheses

def is_valid(s):
    result=[]
    check={'(':')','{':'}','[':']'}
    for i in s:
        if i in check:
            result.append(i)
        else:
            if not result or check[result[-1]]!=i:
                return False
            result.pop()
    return len(result)==0

print(is_valid('([]{(}))'))
print(is_valid('([]{})'))