from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:  # Don't need this. It's handled in the while loop below
            return list2

        if list2 is None:  # Same here. Not needed
            return list1

        # this can be removed by created a dummy placeholder at the head and returning dummy.next at
        # the end..
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next

        output = head
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                next_val = list1.val
                if list1 is not None:  # this check is pointless
                    list1 = list1.next
            else:
                next_val = list2.val
                if list2 is not None:   # this check is pointless
                    list2 = list2.next
            output.next = ListNode(next_val)
            output = output.next

        # don't need to iterate, just set equal..
        lst = list1 if list1 is not None else list2
        while lst is not None:
            output.next = ListNode(lst.val)
            output = output.next
            lst = lst.next

        return head


if __name__ == "__main__":

    list1 = ListNode(-9, ListNode(3))
    list2 = ListNode(5, ListNode(7))
    s = Solution()
    result = s.mergeTwoLists(list1, list2)
    print("result:")
    while result is not None:
        print(result.val)
        result = result.next
