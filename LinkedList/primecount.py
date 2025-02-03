class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
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
    def display(self):
        temp = self.head
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data,end = "-->")
            temp = temp.next
        print("\n")
    def isprime(self, data):
        if data < 2:  # 0 and 1 are not prime
            return False
        for i in range(2, int(data ** 0.5) + 1):  # Check up to √data
            if data % i == 0:
                return False
        return True
    def countprime(self):
        c = 0
        temp = self.head
        if temp is None:
            print("Empty")
        else:
            while temp:
                if self.isprime(temp.data):
                    c = c + 1
                temp = temp.next
        print(f"The Number of Primes : {c}")
                
l = sll()
n = int(input("Enter the number of elements : "))
for i in range(n):
    item = int(input(f"Enter the element {i} : "))
    l.insert_at_end(item)
l.display()
l.countprime()
    