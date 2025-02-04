class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        nn = Node(data)
        if self.head:  
            self.head.prev = nn  
            nn.next = self.head  
        self.head = nn  

    def insert_at_end(self, data):
        if not self.head:  
            self.insert_at_begin(data)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        nn = Node(data)
        temp.next = nn
        nn.prev = temp

    def display(self):
        temp = self.head
        if not temp:
            print("List is Empty")
            return
        
        print("Forward Traversal:")
        while temp:
            print(temp.data, end=" <--> ")
            last = temp  
            temp = temp.next
        print("None")
        
        # Reverse Traversal
        print("Reverse Traversal:")
        while last:
            print(last.data, end=" <--> ")
            last = last.prev
        print("None")

# Driver Code
dll = DLL()
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(element)

dll.display()
