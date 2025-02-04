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
    def sumtobinary(self):
        temp = self.head
        n = 0
        if temp is None:
            print("empty")
            return 
        while temp:
            n = n + temp.data
            temp = temp.next
        binary = format(n,"b")
        print(f"The sum of given list is : {n}")
        print(f"The Binary Number is : {binary}")
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
l.sumtobinary()
print("\n")
l.display()
