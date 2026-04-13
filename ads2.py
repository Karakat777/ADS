class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add to the beginning
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Add to the end
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3. Remove the last element
    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    # 4. Print all elements
    def print_list(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "List is empty")

    # 5. Search for a specific element
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    # 6. Insert at a given position
    def insert_at(self, pos, data):
        if pos == 0:
            self.add_to_start(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if curr:
                curr = curr.next
        if curr:
            new_node.next = curr.next
            curr.next = new_node

    # 7. Remove an element by value
    def remove_by_value(self, val):
        curr = self.head
        if curr and curr.data == val:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != val:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    # 8. Combine two lists
    def combine(self, other):
        if not self.head:
            self.head = other.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other.head

    # 9. Reverse the list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # 10. Sort the list (Insertion Sort)
    def insertion_sort(self):
        sorted_h = None
        curr = self.head
        while curr:
            nxt = curr.next
            if not sorted_h or sorted_h.data >= curr.data:
                curr.next = sorted_h
                sorted_h = curr
            else:
                temp = sorted_h
                while temp.next and temp.next.data < curr.data:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
            curr = nxt
        self.head = sorted_h


print("1 & 2. Creating list and adding 10 (start) and 20 (end):")
llist = LinkedList()
llist.add_to_start(10)
llist.add_to_end(20)
llist.print_list()

print("\n6. Inserting 15 at position 1:")
llist.insert_at(1, 15)
llist.print_list()

print("\n9. Reversing the list:")
llist.reverse()
llist.print_list()

print("\n10. Sorting the list (ascending):")
llist.insertion_sort()
llist.print_list()

print("\n5. Searching for value 15:")
print("Found?" , llist.search(15))

print("\n7. Removing value 15:")
llist.remove_by_value(15)
llist.print_list()

print("\n3. Removing the last element:")
llist.remove_last()
llist.print_list()

# Example for Combine
print("\n8. Combining with another list [100, 200]:")
other_llist = LinkedList()
other_llist.add_to_end(100)
other_llist.add_to_end(200)
llist.combine(other_llist)
llist.print_list()