# FIFO - First In First Out

class Queue:
    # Queue implementation using a list
    
    def __init__(self):
        # Initialize an empty queue
        self.items = []
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0
    
    def enqueue(self, item):
        # Add an item to the back of the queue
        self.items.append(item)
    
    def dequeue(self):
        # Remove and return the front item from the queue
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def size(self):
        # Return the number of items in the queue
        return len(self.items)


# -------------- TESTING ---------------

if __name__ == "__main__":
    # Create a new queue
    q = Queue()
    
    # Enqueue three items
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    
    # Dequeue front item
    print(f"Queue dequeue: {q.dequeue()}")  # Should print 100
    
    # Check size
    print(f"Queue size: {q.size()}")  # Should print 2