# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        num1 = ""
        num2 = ""

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next  # Move to the next node

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next  # Move to the next node

        num1 = int(num1)
        num2 = int(num2)

        total = num1 + num2

        # Return the result in ListNode
        dummy_head = ListNode()
        current = dummy_head
        for digit in str(total)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next  # Skip the dummy node


# Test cases
d3 = ListNode(2)
d2 = ListNode(4, d3)
d1 = ListNode(3, d2)

n3 = ListNode(5)
n2 = ListNode(6, n3)
n1 = ListNode(4, n2)

sol = Solution()

result = sol.addTwoNumbers(d1, n1)
while result:
    print(result.val)
    result = result.next


# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
