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
    def zigzag(self):
        temp = self.head
        l = []
        while temp :
            l.append(temp.data)
            temp =temp.next 
        n = len(l)
        i = 0
        j = n - 1
        m = (i + j) // 2
        i = m - 1
        j = m + 1
        nl = [l[m]]
        while i >= 0 and j < n:
            nl.append(l[i])
            nl.append(l[j])
            i -= 1
            j += 1
        if i >= 0:
            nl.append(l[i])
        if j < n:
            nl.append(l[j])
        temp = self.head
        for val in nl:
            temp.data =  val 
            temp = temp.next
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
l.zigzag()
print("\n")
l.display()