class MinHeap:
    def __init__(self):
        self.heap=[]
    def get_parent(self,i):
        return (i-1)//2
    def get_left(self,i):
        return i*2+1
    def get_right(self,i):
        return i*2+2
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def insert(self,data):
        self.heap.append(data)
        self.up_heap(len(self.heap)-1)
    def up_heap(self,i):
        if i ==0:
            return
        parent=self.get_parent(i)
        if self.heap[i]<self.heap[parent]:
            self.swap(i,parent)
            self.up_heap(parent)
            
x=MinHeap()
x.insert(10)
x.insert(20)
x.insert(30)
x.insert(40)
print(x.heap)