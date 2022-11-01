from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(
            curr: Optional[ListNode], prev: Optional[ListNode]
        ) -> Optional[ListNode]:
            """Recurses through a singly-linked list until it `curr` is `None`.

            Arguments:
            curr: ListNode - current list node
            prev: ListNode - previous list node

            Returns:
            ListNode - Returns the original tail node, which will be the new head node
            """
            if not curr:  # Base Case
                return prev  # return previous, because curr is None

            # Save the next node, because we will replace curr.next
            next_node = curr.next
            curr.next = prev  # curr.next will now point **backwards** to prev

            # recurse to the next_node, update prev with curr
            return recurse(next_node, curr)

        # Will return the tail (new head) once the base case occurs
        return recurse(head, None)

    def print_list(self, head: Optional[ListNode]):
        # Print val of each node (with a next arrow)
        while head.next:
            print(str(head.val) + "->", end="")
            head = head.next  # increment head
        # Prints the very last node (that does not have a next)
        print(head.val)


if __name__ == "__main__":
    # Initialize nodes
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    # Initialize solution object
    s = Solution()
    print("Original Linked List: ", end="")
    s.print_list(head)

    # Call reverseList method
    reverse_head = s.reverseList(head)
    print("Reversed Linked List: ", end="")
    s.print_list(reverse_head)
