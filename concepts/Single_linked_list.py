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
    def duplicate_delete(self):
        lst=[]
        temp=self.head
        while temp.next:
            lst.append(temp.data)
            if temp.next.data in lst:
                temp.next=temp.next.next
            else:
                temp=temp.next
    def sorting(self):
        val=[]
        temp=self.head
        while temp:
            val.append(temp.data)
            temp=temp.next
        val.sort()
        temp=self.head
        for i in val:
            temp.data=i
            temp=temp.next
    def delete_value(self,val):
        if self.head is None:
            return
        if self.head.data==val:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next is not None and temp.next.data!=val:
            temp=temp.next
        if temp.next is not None:
            temp.next=temp.next.next

x=LinkedList()
x.insertion(10)
x.insertion(20)
x.insertion(30)
# x.insertion(30)
# x.insertion_position(99,2)
# x.deletion_position(2)
# x.insert_begining(100)
# x.insert_end(999)
# x.delete_begining()
# x.delete_end()
# x.reverse()
# x.duplicate_delete()
# x.sorting()
# x.delete_value(30)
x.print_list()
# if x.palindrome():
#     print("Palindrome")
# else:
#     print('Not palindrome')




    # ----------------------------------------------------
    # MERGE SORT (BEST SORTING FOR LINKED LISTS)
    # ----------------------------------------------------

    def sort(self):
        self.head = self.merge_sort(self.head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        right = mid.next
        mid.next = None

        left_sorted = self.merge_sort(head)
        right_sorted = self.merge_sort(right)

        return self.merge(left_sorted, right_sorted)

    def get_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, a, b):
        dummy = Node(0)
        tail = dummy

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        return dummy.next
    # ----------------------------------------------------
    # REMOVE DUPLICATES
    # ----------------------------------------------------

    # Sorted list
    def remove_duplicates_sorted(self):
        temp = self.head
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
    # ----------------------------------------------------
    # LOOP DETECTION (FLOYD'S ALGO)
    # ----------------------------------------------------

    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # ----------------------------------------------------
    # REMOVE Nth NODE FROM END
    # ----------------------------------------------------

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head

        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        self.head = dummy.next

    # ----------------------------------------------------
    # REVERSE IN GROUPS OF K
    # ----------------------------------------------------

    def reverse_k_group(self, head, k):
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head

        prev = None
        curr = head
        next_node = None

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverse_k_group(curr, k)
        return prev

    def apply_reverse_k_group(self, k):
        self.head = self.reverse_k_group(self.head, k)

    # ----------------------------------------------------
    # ROTATE LIST (MOVE LAST K NODES TO FRONT)
    # ----------------------------------------------------

    def rotate(self, k):
        if not self.head or k == 0:
            return

        temp = self.head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1

        k %= length
        if k == 0:
            return

        temp.next = self.head  # make it circular

        steps = length - k
        new_tail = self.head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        new_tail.next = None

    # ----------------------------------------------------
    # ADD TWO NUMBERS (LINKED LIST NUMBERS)
    # ----------------------------------------------------

    def add_two_numbers(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            tail.next = Node(total % 10)
            tail = tail.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next