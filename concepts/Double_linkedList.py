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
# to remove all occurences 
        # while self.head and self.head.data==val:
        #     self.head=self.head.next
        #     if self.head:
        #         self.head.prev=None
        # temp=self.head
        # while temp and temp.next:
        #     if temp.next.data==val:
        #         temp.next=temp.next.next
        #         if temp.next:
        #             temp.next.prev=temp
        #     else:
        #         temp=temp.next

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
    def make_circular(self):
        if self.head is None:
            return
        tail=self.head
        while tail.next:
            tail=tail.next
        tail.next=self.head
        self.head.prev=tail
    def print_circular(self):
        if self.head is None:
            return
        temp=self.head
        while True:
            print(temp.data,end='-')
            temp=temp.next
            if temp==self.head:
                break
    def DL_jump(self,k):
        if self.head is None:
            return
        temp=self.head
        while temp:
            print(temp.data,end='-')
            for _ in range(k):
                if temp:
                    temp=temp.next
    # if this is already circular then do this to rotate
    def rotate_circular_left(self,k):
        if self.head is None or k==0:
            return
        tail=self.head
        l=1
        while tail.next!=self.head:
            tail=tail.next
            l+=1
        k=k%l
        if k==0:
            return
        for _ in range(k):
            self.head = self.head.next
    def rotate_circular_right(self,k):
        if self.head is None or k==0:
            return
        tail=self.head
        l=1
        while tail.next!=self.head:
            tail=tail.next
            l+=1
        k=k%l
        if k==0:
            return
        for _ in range(k):
            self.head = self.head.prev

    def rotate_left_linear(self, k):
        if not self.head or k == 0:
            return

        # 1. Find length and tail
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return

        # 2. Connect tail to head temporarily
        tail.next = self.head
        self.head.prev = tail

        # 3. Find new tail (kth node)
        new_tail = self.head
        for _ in range(k - 1):
            new_tail = new_tail.next

        # 4. Set new head and break the ring
        self.head = new_tail.next
        self.head.prev = None
        new_tail.next = None
        
    def rotate_right_linear(self, k):
        if not self.head or k == 0:
            return

        # 1. Find length and tail
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return

        # 2. Connect tail to head temporarily
        tail.next = self.head
        self.head.prev = tail

        # 3. Find new tail (length - k steps forward from head)
        steps = length - k
        new_tail = self.head
        for _ in range(steps - 1):
            new_tail = new_tail.next  # <--- Walk FORWARD by (length - k) steps

        # 4. Set new head and break the ring
        self.head = new_tail.next
        self.head.prev = None
        new_tail.next = None

            
            

        
            
x=LinkedList()
for i in [2,6,1,4,8]:
    x.insertion(i)
# if x.palindrome():
#     print('Palindrome')
# else:
#     print('not')
# x.insert_beginig(99)
# x.insert_position(100,2)
# x.delete_first()
# x.reverse()
# x.sorting()
# x.delete_po(3)
# x.print_list()
# x.make_circular()
# x.rotate_circular_left(2)
x.rotate_circular_right(2)
x.rotate_left_linear(2)
x.rotate_right_linear(2)
x.print_list()
# x.print_circular()