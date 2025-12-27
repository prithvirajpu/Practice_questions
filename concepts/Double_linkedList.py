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
        self.head.prev=None
    
    def delete_po(self,po):
        if po==0:
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            return
        temp=self.head
        count=0
        while temp is not None and count<po:
            temp=temp.next
            count+=1
        if temp.next:
            temp.next.prev=temp.prev
        if temp.prev:
            temp.prev.next=temp.next

    def delete_val(self,val):
        if self.head.data==val:
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            return
        temp=self.head
        while temp.next:
            if temp.next.data ==val:
                temp.next=temp.next.next
                if temp.next:
                    temp.next.prev=temp
            else:
                temp=temp.next

    def reverse(self):
        temp=self.head
        prev=None
        while temp:
            prev=temp.prev
            temp.prev=temp.next
            temp.next=prev
            temp=temp.prev
        if prev:
            self.head=prev.prev
    def sorting(self):
        temp=self.head
        val=[]
        while temp:
            val.append(temp.data)
            temp=temp.next
        val.sort()
        temp=self.head
        for i in val:
            temp.data=i
            temp=temp.next
            
x=LinkedList()
x.insertion(10)
x.insertion(20)
x.insertion(30)
if x.palindrome():
    print('Palindrome')
else:
    print('not')
x.insert_beginig(99)
x.insert_position(100,2)
x.delete_first()
x.reverse()
x.sorting()
x.delete_po(3)
x.print_list()