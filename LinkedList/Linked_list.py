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
    def insert_at_index(self,data,pos):
        temp = self.head
        c = 0
        while temp.next:
            temp = temp.next
            c += 1
        print(c)
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
    l.insertatbegin(t)
l.display()
last = int(input("Enter the last element to be add : "))
l.insertatend(last)
l.display()
data = int(input("Enter the number : "))
pos = int(input("Enter the number : "))
#Harry is a teacher working in a school he has been given a list of roll.no. one of the parent want to meet his child parent gives the id of the student help harry to find the student 
# enter Id,s : 1 2 3 4 5 6 7 8 9 10 
# enter search id : 7
# output : True 
l.insert_at_index(data,pos)