class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        nn = Node(data)
        nn.next = self.head
        self.head = nn

    def insert_at_end(self, data):
        temp = self.head
        if temp is None:
            self.insert_at_begin(data)
        else:
            while temp.next:
                temp = temp.next
            nn = Node(data)
            temp.next = nn

    def sorting(self):
        if self.head is None:
            print("List is empty")
            return

        # Step 1: Extract data into a list
        values = []
        temp = self.head
        while temp:
            values.append(temp.data)
            temp = temp.next

        # Step 2: Sort the list
        values.sort()

        # Step 3: Update the linked list with sorted values
        temp = self.head
        for val in values:
            temp.data = val
            temp = temp.next

    def display(self):
        self.sorting()  # Sort the linked list before displaying
        temp = self.head
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")  # Indicating end of list

# Driver Code
ll = LinkedList()
n = int(input("Enter the number of elements: "))
for i in range(n):
    t = int(input(f"Enter element {i+1}: "))
    ll.insert_at_end(t)

ll.display()

