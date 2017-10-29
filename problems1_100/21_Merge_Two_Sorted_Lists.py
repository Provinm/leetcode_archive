
'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 头结点
        head = l1
        # 移动节点
        prenode = None

        while l2 is not None:
            curnode = head
            newnode = ListNode(l2.val)
            while curnode is not None and curnode.val < l2.val:
                print('cur is ',curnode.val)
                prenode = curnode
                curnode = curnode.next
            if prenode is None:
                newnode.next = head
                head = newnode
            elif curnode is None:
                prenode.next = newnode
            else:
                newnode.next = curnode
                prenode.next = newnode

            l2 = l2.next

        return head

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = None

s = Solution()
res = s.mergeTwoLists(l2,l1)

while res is not None:
    print(res.val)
    res = res.next


'''
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

# in-place, iteratively
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

'''
