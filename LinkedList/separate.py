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
    def separate(self):
        neg = []
        pos = []
        temp = self.head
        if temp is None:
            print("Empty")
        while temp:
            if temp.data >= 0:
                pos.append(temp.data)
            else:
                neg.append(temp.data)
            temp  =temp.next
        temp = self.head
        for val in neg:
            temp.data = val
            temp = temp.next
        for val in pos:
            temp.data = val
            temp = temp.next
    def display(self):
        temp = self.head
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
l = all()
n = int(input("Enter the number : "))
for i in range(n):
    t = int(input("Enter the element : "))
    l.insertatend(t)
l.display()
print("\n")
l.separate()
l.display()
# 