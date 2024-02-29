from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        output = head = ListNode()
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next

        output.next = list1 if list1 is not None else list2

        return head.next


if __name__ == "__main__":

    list1 = ListNode(-9, ListNode(3))
    list2 = ListNode(5, ListNode(7))
    s = Solution()
    result = s.mergeTwoLists(list1, list2)
    print("result:")
    while result is not None:
        print(result.val)
        result = result.next
