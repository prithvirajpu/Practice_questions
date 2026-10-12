import heapq

tasks = []

heapq.heappush(tasks, (2, "Normal task"))
heapq.heappush(tasks, (1, "Urgent task"))
heapq.heappush(tasks, (3, "Low priority task"))
print(tasks)

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)