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

    def minValue(self, node):
        current = node
        while current.left:   # keep going left to find min
            current = current.left
        return current.data

            
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

x=BST()
# x.insert(10)
# x.insert(20)
# x.insert(30)
# x.insert(40)
# x.insert(8)
arr=[1,2,3,4,5,6]
x.sortedarray_to_BST(arr)
print(x.search(x.root,40))
print(x.search(x.root,60))
x.preorder(x.root)
print()
x.postorder(x.root)
print()
x.deleteNode(x.root,10)
x.inorder(x.root)