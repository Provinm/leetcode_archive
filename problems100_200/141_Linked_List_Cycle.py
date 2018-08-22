#coding=utf-8

'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        hash_dict = {}
        while head:
            
            if head in hash_dict:
                return head

            else:
                hash_dict[head] = 1

            head = head.next

        return False
                
                

