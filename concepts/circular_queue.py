class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1

        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

        print(f"Dequeued: {value}")
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue elements:", end=" ")

        for i in range(self.count):
            index = (self.front + i) % self.size
            print(self.queue[index], end=" ")

        print()


# Example usage
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

cq.dequeue()
cq.dequeue()

cq.enqueue(50)
cq.enqueue(60)

cq.display()

print("Front element:", cq.peek())