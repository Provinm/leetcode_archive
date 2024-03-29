# coding=utf-8

'''
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curnode = head
        while curnode and curnode.next:

            while curnode.next and curnode.val == curnode.next.val:
                curnode.next = curnode.next.next
                # curnode = curnode.next

            curnode = curnode.next

        return head
