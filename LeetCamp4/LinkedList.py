import copy


class Node:
    """A node in a singly-linked list."""

    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val)

    def remove(self):
        if self.head is None:
            return

        curr = self.head
        prev = None
        while curr:
            if curr.next is None:
                prev.next = None
                del curr
                return
            prev = curr
            curr = curr.next

    def print_list(self):
        if self.head is None:
            print("The list is empty")
            return

        output = ""
        curr = self.head
        while curr.next:
            output += str(curr.data) + "->"
            curr = curr.next
        output += str(curr.data)
        print(output)

    def search(self, pos):
        """Print the data of a node at a given position. `pos` is assuming 0 indexed."""
        if self.head is None:
            return None

        curr = self.head
        i = 0
        while curr.next:
            if i == pos:
                return curr
            curr = curr.next
        return None


def createLinkedList(head):
    # account for empty list
    if head is None:
        print("list is empty")
        return

    dummy = Node()
    dummy.next = head.next

    dummyOdd = Node()
    dummyOdd.next = copy.deepcopy(head)

    curr_new = dummyOdd.next
    curr_old = head.next
    prev = None
    while curr_old and curr_old.next:
        i = 1
        while curr_old and curr_new:
            if i % 2 == 0:  # even
                print("Even", curr_old.data)
                curr_old.next = curr_new.next
                curr_old = curr_old.next
            else:  # odd
                print("Odd", curr_new.data)
                curr_new.next = curr_old.next
                prev = curr_new
                curr_new = curr_new.next
            i += 1

        curr_old = dummy.next
        curr_new = prev

    curr_new.next = curr_old

    return dummyOdd.next


LL = LinkedList()

for x in [5, 2, 8, 7, 3, 1, 9]:
    LL.append(x)

print("Original list:")
LL.print_list()

oddListHead = createLinkedList(LL.head)

print("\nOdd only:")
oddList = LinkedList()
oddList.head = oddListHead
oddList.print_list()
