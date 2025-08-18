# Double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    # Insertion
    def insertion(self,data):
        new_node=Node(data)
        if self.head is None:
             self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    
    # Insertion at begining
    def insert_beginig(self,data):
        new_node=Node(data)
        temp=self.head
        self.head=new_node
        new_node.next=temp
        temp.prev=new_node

    # Insertion at end
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    # Insertion at certain position
    def insert_position(self,data,index):
        new_node=Node(data)
        if index==0:
            temp=self.head
            self.head=new_node
            new_node.next=temp
            temp.prev=new_node
            return
        temp=self.head
        count=0
        while temp is not None and count<index-1:
            temp=temp.next
            count+=1
        new_node.next=temp.next
        if temp.next:
            temp.next.prev=new_node
        temp.next=new_node
        new_node.prev=temp

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next

    # Palindrome check
    def palindrome(self):
        if self.head.next is None:
            return True
        left=self.head
        right=self.head
        while right.next:
            right=right.next
        while left!=right and left.prev!=right:
            if left.data!=right.data:
                return False
            left=left.next
            right=right.prev
        return True
    def delete_first(self):
        self.head=self.head.next

x=LinkedList()
x.insertion(10)
x.insertion(20)
x.insertion(10)
if x.palindrome():
    print('Palindrome')
else:
    print('not')
x.insert_beginig(99)
x.insert_position(100,2)
x.delete_first()
x.print_list()