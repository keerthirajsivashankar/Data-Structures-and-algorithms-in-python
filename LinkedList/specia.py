class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            nn.next = nn  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = nn
            nn.next = self.head
            self.head = nn

    def insert_at_end(self, data):
        nn = Node(data)
        if self.head is None:
            self.insert_at_begin(data)
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = nn
            nn.next = self.head

    def delete_node(self, target):
        if self.head is None:
            return

        temp = self.head
        prev = None

        if temp.data == target and temp.next == self.head:
            self.head = None
            return

        if temp.data == target:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return

        while temp.next != self.head and temp.data != target:
            prev = temp
            temp = temp.next

        if temp.data == target:
            prev.next = temp.next

    def game(self, k):
        temp = self.head

        while temp.next != temp:  
            for _ in range(k - 1):  
                temp = temp.next
            print(f"Eliminated: {temp.data}")
            self.delete_node(temp.data)  
            temp = temp.next  

        print(f"Winner: {temp.data}")  

    def display(self):
        if not self.head:
            print("List is empty!")
            return

        temp = self.head
        while True:
            print(temp.data, end=" --> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"(Back to {self.head.data})")

# Driver Code
csll = CSLL()
n = int(input("Enter the number of players: "))
for i in range(1, n + 1):
    csll.insert_at_end(i)

k = int(input("Enter the step count (k): "))
csll.display()
csll.game(k)
