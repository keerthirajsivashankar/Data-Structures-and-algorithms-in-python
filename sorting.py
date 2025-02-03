class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class all():
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        nn = node(data)
        self.head = nn
        nn.next = None
    def insert_at_end(self,data):
        temp = self.head
        if temp is None:
            self.insert_at_begin(data)
        else:
            while temp.next:
                temp = temp.next
            nn = node(data)
            temp.next = nn
            nn.next = None
    def sorting(self):
        if self.head is None or self.head.next is None:
            return self.head
        d = node(0)
        curr = self.head
        while curr:
            prev = d
            next_node = curr.next
            while prev.next and prev.next.data < curr.data:
                prev = prev.next
            curr.next = prev.next 
            prev.next = curr 
            curr = next_node
        self.head = d.next
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        else:
            while temp:
                print(temp.data,end = "-->")
                temp = temp.next
            print("\n") 
            
l = all()
n = int(input("Enter the number of students : "))
for i in range(n):
    element = int(input("Enter the role number : "))
    l.insert_at_end(element)
l.sorting()
l.display()
        