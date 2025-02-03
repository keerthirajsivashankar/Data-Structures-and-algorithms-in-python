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
            nn =  node(data)
            while temp.next:
                temp = temp.next
            temp.next = nn
            nn.next = None
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
    def find(self,fdata):
        c = 0
        temp = self.head
        while temp:
            if temp.data == fdata:
                print("Found the data!")
                c = c + 1
                break
            temp = temp.next
        if c == 0 :
            print("The value is not found")
l = all()
n = int(input("Enter the number of students : "))
for i in range(n):
    element = int(input("Enter the role number : "))
    l.insert_at_end(element)
finddata = int(input("Enter the id to search : "))
l.find(finddata)
                
        
        
            