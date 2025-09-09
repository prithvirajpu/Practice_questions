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
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # move last element to root
        self.down_heap(0)
        return root

    def down_heap(self, index):
        smallest = index
        left = self.get_left(index)
        right = self.get_right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.down_heap(smallest)
            
x=MinHeap()
x.insert(40)
x.insert(10)
x.insert(20)
x.insert(30)
x.remove()
print(x.heap)