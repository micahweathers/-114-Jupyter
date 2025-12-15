# LIFO = Last In First Out

class Stack:
    # Stack implementation using a list
    
    def __init__(self):
        # Initialize an empty stack
        self.items = []
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
    
    def push(self, item):
        # Add a new item to the top of the stack
        self.items.append(item)
    
    def pop(self):
        # Remove and return the top item from the stack
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        # Return the number of items in the stack
        return len(self.items)


# -------------- TESTING ---------------

if __name__ == "__main__":
    # Create a new stack
    s = Stack()
    
    # Push three items
    s.push(1)
    s.push(2)
    s.push(3)
    
    # Peek at top item
    print(f"Stack peek: {s.peek()}")  # Should print 3
    
    # Pop the top item
    print(f"Stack pop: {s.pop()}")  # Should print 3
    
    # Check size
    print(f"Stack size: {s.size()}")  # Should print 2