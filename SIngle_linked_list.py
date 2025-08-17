# SIngle linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    # Insertion at begining
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        self.head=new_node
        new_node.next=temp
    
    # Insert at End
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node


    # Insertion of data--------
    def insertion(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print()

    # Insertion to a specific position
    def insertion_position(self,data,index):
        new_node=Node(data)
        if index==0:
            new=self.head
            self.head=new_node
            new_node.next=new
            return
        count=0
        temp=self.head
        while temp is not None and count<index-1:
            temp=temp.next
            count+=1
        new_node.next=temp.next
        temp.next=new_node

    # Deletion from a specific position
    def deletion_position(self,index):
        if index==0:
            self.head=None
            return
        temp=self.head
        count=0
        while temp  is not None and count<index-1:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
    
    # Deletion in begining
    def delete_begining(self):
        self.head=self.head.next

    # Delete at the end
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=temp.next.next
    
    # Palindrome checking
    def palindrome(self):
        temp=self.head
        val=[]
        while temp:
            val.append(temp.data)
            temp=temp.next
        return val==val[::-1]
    def reverse(self):
        temp=self.head
        prev=None
        while temp:
            save=temp.next
            temp.next=prev
            prev=temp
            temp=save
        self.head=prev
    def find_middle(self):
        slow=self.head
        fast=self.head
        # check=None
        while fast and fast.next:
            fast=fast.next.next
            # check=slow
            slow=slow.next
        print(f'Middle node is {slow.data}')
        # for deleting the middle one
        
        # check.next=slow.next
        # slow.next.prev=check

x=LinkedList()
x.insertion(10)
x.insertion(20)
x.insertion(30)
x.insertion_position(99,2)
x.deletion_position(2)
x.insert_begining(100)
x.insert_end(999)
x.delete_begining()
x.delete_end()
x.reverse()
x.print_list()
if x.palindrome():
    print("Palindrome")
else:
    print('Not palindrome')