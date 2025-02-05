class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class sll():
    def __init__(self):
        self.head = None
    def push(self,data):
        nn = node(data)
        nn.next = self.head
        self.head = nn
    def pop(self):
        self.head = self.head.next
    def peek(self):
        temp = self.head
        if temp is None:
            print("stack is empty")
        else:
            print(f"The top element is : {temp.data}")
    def isprime(self,data):
        if data < 2:
            return False
        else:
            for i in range(2, int(data ** 0.5) + 1):  
                if data % i == 0:
                    return False
        return True
    def splitprime(self,data):
        if data < 10:
            return True
        else:
            data = list(str(data))
            n = len(data)
            c = 0
            for i in range(n):
                if self.isprime(int(data[i])):
                    c = c + 1
            return c == n 
            
    def countandprint(self):
        temp = self.head
        if temp is None:
            print("The stack is empty ")
        else:
            i = 0
            c = 0
            res = []
            while temp:
                if self.isprime(temp.data):
                    if self.splitprime(temp.data):
                        res.append([i,temp.data])
                        c += 1
                i += 1
                temp = temp.next
            print(f"\nThe count of prime : {c}\n")
            print(f"The pairs of prime with index : {res}\n")
            
    
    def display(self):
        temp = self.head
        if temp is None:
            print("The list isb empty")
        else:
            while temp:
                print(f"\t | {temp.data} |",end="\n")
                print("\t -----")
                temp = temp.next
            print("\n")
#driver code:
l = sll()
n = int(input("Enter the number of elemwnts to be added : "))
for i in range(n):
    l.push(int(input("Enter the data : ")))
l.display()
l.countandprint()