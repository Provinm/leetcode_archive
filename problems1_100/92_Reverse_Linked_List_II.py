#coding=utf-8
'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy_node = ListNode(-1)
        dummy_node.next = head

        cur_node = dummy_node
        pre_m_node = None
        m_node = None
        dynamic_node = None
        n_node = None
        after_n_node = None
        
        for i in range(m-1):
            cur_node = cur_node.next

        pre_m_node = cur_node
        m_node = pre_m_node.next
        dynamic_node = m_node
        cur_node = m_node.next

        idx = m
        while idx < n:
            process_node = cur_node
            cur_node = cur_node.next

            process_node.next = dynamic_node
            dynamic_node = process_node

            idx += 1

        after_n_node = cur_node
        pre_m_node.next = dynamic_node
        m_node.next = after_n_node

        return dummy_node.next


def gen_linknode(lst):
    
    head = None
    f = None
    while lst:
        # print(lst)
        item = lst.pop(0)
        ln = ListNode(item)
        if not f:
            f = ln
            head = ln
        else:
            f.next = ln
            f = f.next

    return head

def display_ln(f):
    
    s = []
    while f:
        s.append(f.val)
        f = f.next

    return s

lst = [1,2]
m = 1
n = 1

head = gen_linknode(lst)
print(display_ln(head))

s = Solution()
res = s.reverseBetween(head, m, n)
print(display_ln(res))





            




