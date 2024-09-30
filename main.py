from MUQueue import MUQueue

queue = MUQueue() # initializing queue

# enqueue values 1, 2, 45, 50
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(45)
queue.enqueue(50)
print(queue) # printing enqueued values


# dequeue values 1 and 2
queue.dequeue()
queue.dequeue()
print(queue) # printing new queue


queue.enqueue(67) # enqueue 67
print(queue)


print(queue.peek()) # printing the first item in queue


print(queue.size()) # printing length of the queue