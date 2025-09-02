class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
    def _insert(self,temp,data):
        if data<temp.data:
            if temp.left is None:
                temp.left=Node(data)
            else:
                self._insert(temp.left,data)
        elif data>temp.data:
            if temp.right is None:
                temp.right=Node(data)
            else:
                self._insert(self.right,data)

x=BST()
x.insert(10)
x.insert(120)
