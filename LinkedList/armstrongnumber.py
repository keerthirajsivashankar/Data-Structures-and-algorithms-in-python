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
    def armstrong(self,data):
        temp = data 
        data = list(str(data))
        p = len(data)
        arm = 0
        for c in data:
            c = int(c)
            c = c ** p
            arm = arm + c
        return temp == arm
    def countarmstrong(self):
        temp = self.head
        c = 0
        i = 0
        res = []
        if temp is None:
            print("Empty")
        while temp:
            if self.armstrong(temp.data):
                c = c+1
                res.append([i,temp.data])
            i = i + 1
            temp = temp.next
        print(f"The Number of armstrong number : {c}",end="\n")
        print(f"The list of armstrong number : ",res,end="\n")
    def display(self):
        temp = self.head
        print("The linked List is : ",end="\n")
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
l = all()
n = int(input("Enter the number of elements : "))
for i in range(n):
    ele = int(input("Enter the element : "))
    l.insertatend(ele)
l.display()
print("\n")
l.countarmstrong()