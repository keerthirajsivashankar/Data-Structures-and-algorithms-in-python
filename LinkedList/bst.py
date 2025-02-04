class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedListToBST:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(data)

    def find_middle(self, start, end):
        slow = fast = start
        prev = None
        while fast != end and fast.next != end:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow  

    def sorted_list_to_bst(self, start, end):
        if start == end:
            return None

        prev, mid = self.find_middle(start, end)

        root = TreeNode(mid.data)
        root.left = self.sorted_list_to_bst(start, mid)  
        root.right = self.sorted_list_to_bst(mid.next, end)  

        return root

    def convert_to_bst(self):
        return self.sorted_list_to_bst(self.head, None)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=" ")  
            self.preorder_traversal(root.left)  
            self.preorder_traversal(root.right)  

# Driver Code
ll = LinkedListToBST()
elements = [10, 20, 30, 40, 50]  

for item in elements:
    ll.insert_at_end(item)

print(" the required solution :")
bst_root = ll.convert_to_bst()
ll.preorder_traversal(bst_root)  
