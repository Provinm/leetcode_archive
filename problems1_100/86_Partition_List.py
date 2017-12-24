#coding=utf-8
'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        h1 = l1 = ListNode(-1)
        h2 = l2 = ListNode(-1)
        while head:
            
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next

            head = head.next
        l2.next = None
        l1.next = h2.next   
        return h1.next

def struct(lst):
    dummy = ListNode(-1)
    head = dummy
    for i in lst:
        new = ListNode(i)
        dummy.next = new
        dummy = dummy.next


    return head.next

def extract(node):

    # print(node.val)
    res = []
    while node:
        res.append(node.val)
        node = node.next

    return res

lst = [1,4,3,2,6,5,2]
target = 3
list_node = struct(lst)
# print(extract(list_node))
s = Solution()
r = s.partition(list_node, target)

print(extract(r))