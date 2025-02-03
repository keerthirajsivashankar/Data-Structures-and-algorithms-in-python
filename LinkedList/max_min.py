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
    def maxx(self):
        temp = self.head
        maax = float('-inf') 
        if temp is None:
            print("Enter the elements First : ")
            return
        while temp:
            if maax < temp.data:
                maax = temp.data
            temp = temp.next
            
        print(f"The maximum element of the list : {maax}")
    def minn(self):
        temp = self.head
        miin = float('inf')
        if temp is None:
            print("Enter the elements first")
            return
        while temp:
            if miin > temp.data:
                miin = temp.data
            temp = temp.next
        print(f"The minimum Value of the list : {miin}")
l = all()
n = int(input("Enter the number of students : "))
for i in range(n):
    element = int(input("Enter the role number : "))
    l.insert_at_end(element)
l.maxx()
l.minn()

            
            
        