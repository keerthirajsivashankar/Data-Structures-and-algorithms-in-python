class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
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
