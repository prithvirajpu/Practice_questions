class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
class GTree:
    def __init__(self,data):
        self.root=Node(data)
    def add_node(self,parent,data):
        parent=self.search(parent)
        if parent:
            parent.children.append(Node(data))
        else:
            print('not found')
    def search(self,parent,node=None):
        if node is None:
            node=self.root
        if node.data==parent:
            return node
        for i in node.children:
            found=self.search(parent,i)
            if found:
                return found
        return None
    def dfs(self,node=None):
        if node is None:
            node=self.root
        print(node.data)
        for i in node.children:
            self.dfs(i)
x=GTree(20)
x.add_node(20,5)
x.add_node(20,6)
x.add_node(20,7)
x.add_node(7,10)
x.add_node(7,11)
x.add_node(7,12)
x.dfs()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Btree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left is None:    
                current.left=new_node
                break
            else:
                queue.append(current.left)
            if current.right is None:
                current.right=new_node
                break
            else:
                queue.append(current.right)
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end='-')
        self.inorder(root.right)
    def height(self,node=None):
        if node is None:
            node=self.root
            if node is None:
                return -1
        if node.left is None and node.right is None:
            return 0
        left=self.height(node.left) if node.left else -1
        right=self.height(node.right) if node.right else -1
        return max(left,right)+1
    
y=Btree()
y.insert(10)
y.insert(90)
y.insert(70)
y.insert(80)
y.inorder(y.root)
print(y.height())

