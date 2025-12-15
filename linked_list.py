class Node:
    # Node class - each node holds a value and a pointer to the next node
    
    def __init__(self, value):
        # Initialize a node with a value and next pointer set to None
        self.value = value
        self.next = None


class LinkedList:
    # Single Linked List implementation
    
    def __init__(self):
        # Initialize an empty linked list with head set to None
        self.head = None
    
    def append(self, value):
        # Add a new node to the end of the list
        new_node = Node(value)
        
        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next is not None:
                current = current.next
            # Connect the new node at the end
            current.next = new_node
    
    def print_list(self):
        # Print all values in the linked list
        current = self.head
        
        # Check if list is empty
        if current is None:
            print("List is empty")
            return
        
        # Walk through the list and print each value
        while current is not None:
            print(current.value)
            current = current.next
    
    def count_nodes(self):
        # Count and return the number of nodes in the list
        count = 0
        current = self.head
        
        # Walk through the list and count each node
        while current is not None:
            count += 1
            current = current.next
        
        return count
    
    def prepend(self, value):
        # Insert a new node at the beginning of the list
        new_node = Node(value)
        # Point new node's next to current head
        new_node.next = self.head
        # Update head to be the new node
        self.head = new_node
    
    def remove(self, value):
        # Remove the first node whose value matches the given value
        # If list is empty, do nothing
        if self.head is None:
            return
        
        # If the head is the node to remove
        if self.head.value == value:
            self.head = self.head.next
            return
        
        # Walk through the list to find the node to remove
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                # Skip the node by connecting to the node after it
                current.next = current.next.next
                return
            current = current.next


# -------------- TESTING ---------------

if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    
    # Add three values
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    print("Original list:")
    ll.print_list()
    
    print(f"\nCount nodes: {ll.count_nodes()}")
    
    # Prepend a value
    ll.prepend(5)
    print("\nAfter prepending 5:")
    ll.print_list()
    
    # Remove a value
    ll.remove(20)
    print("\nAfter removing 20:")
    ll.print_list()
    
    print(f"\nFinal count: {ll.count_nodes()}")