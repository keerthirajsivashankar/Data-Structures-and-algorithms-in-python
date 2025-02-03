class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class sll():
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        nn = node(data)
        nn.next = self.head
        self.head = nn 
    def insert_at_end(self,data):
        temp = self.head
        if temp is None :
            self.insert_at_begin(data)
        else:
            while temp.next:
                temp = temp.next
            nn = node(data)
            temp.next = nn
    def display(self):
        temp = self.head
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data,end = "-->")
            temp = temp.next
        print("\n")
    def rotate(self):
        if not self.head or not self.head.next:  # If list is empty or has one node
            return
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        temp.next = self.head
        self.head = temp
l = sll()
n = int(input("Enter the number of elements : "))
for i in range(n):
    item = int(input(f"Enter the element {i} : "))
    l.insert_at_end(item)
k = int(input("Enter the k : "))
l.display()
for i in range(k):
    l.rotate()
l.display()
