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
    def palindrome(self):
        if self.head is None or self.head.next is None:
            return True
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        left, right = self.head, prev
        while right:  
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True  


l = sll()
n = int(input("Enter the number of elements : "))
for i in range(n):
    item = int(input(f"Enter the element {i} : "))
    l.insert_at_end(item)
l.display()
print("Palindrome : " , l.palindrome() )
