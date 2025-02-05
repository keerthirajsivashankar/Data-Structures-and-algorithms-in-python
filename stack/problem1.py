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
inf = 1
l = sll()
while inf :
    print("Please choose the options \n\t 1.push \n\t 2.pop \n\t 3.peek \n\t 4.isempty \n\t 5.exit \n")
    c = int(input("Enter the choice : "))
    match c:
        case 1:
            l.push(int(input("Enter the element to add : ")))
        case 2:
            l.pop()
        case 3:
            l.peek()
        case 4:
            l.display()
        case 5:
            inf = 0
        case _:
            print("please enter the valid number form 1 - 5")
            

