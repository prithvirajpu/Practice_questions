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
    def symmetric(self,root):
        if not root:
            return True
        def check(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data!=right.data:
                return False
            return check(left.left,right.right)and check(left.right,right.left)
        return check(root.left,root.right)
    def LowestCommonAncestor(self,root,p,q):
        if root is None or p==root or q==root:
            return root
        left=self.LowestCommonAncestor(root.left,p,q)
        right=self.LowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right
    def search(self,root,val):
        if root is None:
            return None
        if root.data == val:
            return root
        
        left = self.search(root.left, val)
        if left:
            return left
        
        return self.search(root.right, val)



y=Btree()
y.insert(10)
y.insert(90)
y.insert(70)
y.insert(80)
p=y.search(y.root,80)
q=y.search(y.root,70)
ans=y.LowestCommonAncestor(y.root,p,q)
print('lca',ans.data)
y.inorder(y.root)
print(y.height())

