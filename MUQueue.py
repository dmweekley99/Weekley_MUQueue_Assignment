from Node import Node

class MUQueue:
    def __init__(self):
        self.head = None  # Front of the queue
        self.tail = None  # End of the queue
        self.length = 0   # Track the size of the queue

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        if values:
            return " -> ".join(values) 
        else:
            "Queue is empty."

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:  # If the queue is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Add new node at the end
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.head is None:  # If the queue is empty
            return "Queue is empty."
        dequeued_value = self.head.value  # Get the value to dequeue
        self.head = self.head.next  # Move the head to the next node
        if self.head is None:  # If the queue is now empty, reset tail to None
            self.tail = None
        self.length -= 1
        return dequeued_value

    def peek(self):
        if self.head is None:  # If the queue is empty
            return 'Queue is empty'
        else:
            return f'Next value in queue is: {self.head.value}'  # Return the value at the front without removing it

    def size(self):
        return f'Queue size is: {self.length}'  # Return the size of the queue