class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class csll:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        nn = node(data)
        if self.head is None:
            self.head = nn
            nn.next = nn
        else:
            temp = self.head
            while temp.next != self.head :
                temp = temp.next
            temp.next = nn
            nn.next = self.head
            self.head = nn
    def insert_at_end(self,data):
        nn = node(data)
        if self.head is None:
            self.insert_at_begin(data)
        else:
            temp = self.head
            while temp.next != self.head :
                temp = temp.next
            temp.next = nn
            nn.next = self.head
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
        
csll = csll()
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    csll.insert_at_end(element)

csll.display()
