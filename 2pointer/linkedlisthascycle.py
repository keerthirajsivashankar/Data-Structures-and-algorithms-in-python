class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class all():
    def __init__(self):
        self.head = None
    def insertatbegin(self,data):
        nn = node(data)
        nn.next = self.head
        self.head = nn
    def insertatend(self,data):
        temp = self.head
        if temp is None:
            self.insertatbegin(data)
        else:
            while temp.next:
                temp = temp.next
            nn = node(data)
            temp.next = nn
    def hasCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return print(True)

        return print(False)
    
    def createcycle(self):
        temp = self.head
        v = self.head.next
        while temp.next:
            temp = temp.next
        temp.next = v
l = all()
n = int(input("Enter the number of elements : "))
for i in range(n):
    ele = int(input("Enter the element : "))
    l.insertatend(ele)
l.createcycle()
l.hasCycle()
print("\n")
