#in this file we will track a lot fo types of queues
#1 simple Queue (Standard FIFO Queue)
print("1 simple Queue")
from collections import deque
import queue
#to create a deck we type
q=deque()
#enqueue items 
q.append("task1") # Rear: Task 1
q.append("task2") # Rear: Task 1 Task 2
q.append("task3") # Rear: Task 1 Task 2 Task 3
print(q)
#dequeue  take off an elemnt from the list (never gets back to its postition)
print(q.popleft())  # this will pop out the first item at the front which is task1
print(q)
#peek : we can peek at the queue and see the frontitem that we will pop next
print(q[0])
# funny and cool BUT we have some Pros/Cons: its simple and fast; but no way to prioritize or access both ends
#with simple queue we enqueue with .append(item)  dequeue with popleft()  and peek at front line with q[0]
print(" 2 Priority Queue")
#Priority Queue : this queue type adds a twist: items have priorities, so higher-priority items are dequeued first, even if they were added later. It's like a hospital waiting room where emergencies jump the line.
#we create a priority queue with  .priorityQueue()
PR=queue.PriorityQueue()
# we enqueue items with priority (lower number = higher priority)
#to enqueue an item we use .put((number that refer to priority   ,   item))
PR.put((2,"buying clothes"))    #priority 2
PR.put((1,"buying courses"))     #priority 1 
PR.put((3,"buying snacks"))     #priority 3
#to dequeue and get the highest priority item we use .get()
print(PR.get())    #buying courses
print(PR.get())    #buying clothes
print(PR.get())    #buying snacks
print(" 3 circular Queue")
#Circular Queue: this is a fixed-size queue where the ends "wrap around" like a circle. When full, adding a new item overwrites the oldest (or blocks). It's efficient for buffers with limited space.
cq=deque(maxlen=3)   #we fixed the size
#enqueue with .apppend()
cq.append(1)   #[1]
print(cq)
cq.append(2)   #[1,2]
print(cq)
cq.append(3)   #[1,2,3]
print(cq)
cq.append(4)   #[2,3,4]   overwrite oldest(1)     comes from the right and 1 exit from the left
print(cq)
#dequeue
print(cq.popleft())       #i takes off 2 
print(cq)
#good . Pros/Cons: Memory-efficient for fixed sizes; but can't grow, and implementation can be tricky without deque.
print("4/ deque : double ended queue")
#deque : this is a queue that allows additions/removals from both ends. It's more flexible than a standard queue.
dq=deque([1,2,3])
#we can enqueue from the front and back(rear) to enque from the front we use deque.appendleft(val) |||| to append from the rear
dq.append(5)
dq.appendleft(0)
print(dq)
#we can popout items from the deque  popleft() we extract the first element on the front  ||| to pop element from the rear we use pop
print(dq.popleft())
print(dq)
print(dq.pop())
print(dq)