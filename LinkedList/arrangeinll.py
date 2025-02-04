class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def rearrange_middle_front(self):
        if not self.head or not self.head.next or not self.head.next.next:
            return  # If list has less than 3 elements, do nothing

        # Find middle element and its previous node
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next  # Middle node (30)
            fast = fast.next.next

        # `slow` is now at the middle element (30)
        if prev and slow.next:
            before = prev  # Node before middle (20)
            after = slow.next  # Node after middle (40)
            first = self.head  # First node (10)

            # Detach middle node (30) from its original position
            prev.next = after  # 20 → 40 (skipping 30)

            # Move 30 to the front
            slow.next = first  # 30 → 10
            self.head = slow  # Update head to 30

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

# Driver Code
ll = LinkedList()
n = int(input("Enter the number : "))
for i in range(n):
    element = int(input("Enter the element : "))
    ll.insert_at_end(element)

print("Original Linked List:")
ll.display()

ll.rearrange_middle_front()

print("Modified Linked List:")
ll.display()
