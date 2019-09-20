#合并两个有序链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        new_list = ListNode(0)
        pre = new_list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 is not None:
            pre.next = l1
        else:
            pre.next = l2
        return new_list.next
        
        
#递归
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        return ret


