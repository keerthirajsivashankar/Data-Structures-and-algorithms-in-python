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
    def display(self):
        temp = self.head
        if temp is None:
            print("The list isb empty")
        else:
            while temp:
                print(f" | {temp.data} |",end="\n")
                print(" -----")
                temp = temp.next
            print("\n")
#driver code:
l = sll()
n = int(input("Enter the number of elemwnts to be added : "))
for i in range(n):
    l.push(int(input("Enter the data : ")))
l.display()
l.peek()
l.pop()
l.display()
