from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    
    # insertion
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        else:
            self._insert(self.root,data)
    def _insert(self,root,data):
        if data<root.data:
            if root.left is None:
                root.left=Node(data)
            else:
                self._insert(root.left,data)
        elif data>root.data:
            if root.right is None:
                root.right=Node(data)
            else:
                self._insert(root.right,data)

    # Searching
    def search(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        elif data<root.data:
            return self.search(root.left,data)
        elif data>root.data:
            return self.search(root.right,data)
        
    #  preorder
    #  postorder
    #  inorder
    def preorder(self,root):
        if root is None:
            return
        print(root.data, end='-')
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end='-')
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end='-')
        self.inorder(root.right)
    def is_empty(self):
        return self.root is None
    def level_order(self):
        if self.is_empty():
            print("Empty")
            return
        queue = deque([self.root])   # use deque for efficient pops
        while queue:
            current = queue.popleft()
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def deleteNode(self, root, data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        else:
            # Case 1: No children (leaf node)
            if root.left is None and root.right is None:
                return None

            # Case 2: One child (right)
            elif root.left is None:
                return root.right

            # Case 2: One child (left)
            elif root.right is None:
                return root.left

            # Case 3: Two children
            else:
                mindata = self.minValue(root.right)  # find inorder successor
                root.data = mindata                  # replace value
                root.right = self.deleteNode(root.right, mindata)  # delete successor
        return root
    
    # Find out the minimum val from the BST - the node is root when calling manually
    def minValue(self, node):
        if node is None:
            return
        while node.left:   # keep going left to find min
            node = node.left
        return node.data

    # Find out the maximum val from the BST- the node is root when calling manually
    def max_val(self,node):
        if node is None:
            return None
        while node.right:
            node=node.right
        return node.data

            
    def sortedarray_to_BST(self,arr):
        if not arr:
            return None
        self.root=self.converter(arr,0,len(arr)-1)
    def converter(self,arr,start,end):
        if start>end:
            return None
        mid=(start+end)//2
        node=Node(arr[mid])
        node.left=self.converter(arr,start,mid-1)
        node.right=self.converter(arr,mid+1,end)
        return node
    
    # checking is it a Binary search tree or not

    def is_bst(self,root,mini=float('-inf'),maxi=float('inf')):
        if root is None:
            return True
        if root.data<=mini or root.data>=maxi:
            return False
        return (self.is_bst(root.left,mini,root.data) and self.is_bst(root.right,root.data,maxi) )
    
    # Find the closest value to the target
    
    def closest(self,root,target):
        if root is None:
            return None
        closest=root.data
        while root is not None:
            if abs(target-root.data) < abs(target-closest):
                closest=root.data
            if target<root.data:
                root=root.left
            elif target>root.data:
                root=root.right
            else:
                break
        return closest
    
    def inorder_for_large(self,root,arr):
        if root is None:
            return None
        self.inorder_for_large(root.left,arr)
        arr.append(root.data)
        self.inorder_for_large(root.right,arr)
        
    def sec_largest(self,root):
        if root is None:
            return None
        arr=[]
        self.inorder_for_large(root,arr)
        if len(arr)<2:
            return None
        return arr[-2]
    
    def max_height(self,root):
        if root is None:
            return 0
        return 1+max(self.max_height(root.left),self.max_height(root.right))
    def mini_height(self,root):
        if root is None:
            return 0
        if root.left is None:
            return 1+self.mini_height(root.right)
        if root.right is None:
            return 1+self.mini_height(root.left)
        return 1+min(self.mini_height(root.left),self.mini_height(root.right))

x=BST()
# x.insert(10)
# x.insert(20)
# x.insert(30)
# x.insert(40)
# x.insert(8)
arr=[20,11,21,22,23,24,25,26]
for i in arr:
    x.insert(i)
# x.sortedarray_to_BST(arr)
# print(x.search(x.root,40))
# print(x.search(x.root,60))
# x.preorder(x.root)
# print()
# x.postorder(x.root)
# print()
# x.root=x.deleteNode(x.root,6)
# x.inorder(x.root)
# print(x.is_bst(x.root))
print(x.closest(x.root,10))
x.level_order()
print('second largest' ,x.sec_largest(x.root))
print(x.max_height(x.root))
print(x.mini_height(x.root))
