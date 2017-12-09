#coding=utf-8
'''

82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head: return head
        dummy = ListNode(-1)
        dummy.next = head

        last_node = dummy
        cur_node = head
        next_node = cur_node.next

        while next_node:
            
            is_in_while = False
            while next_node and next_node.val == cur_node.val:
                cur_node.next = next_node.next
                next_node = next_node.next
                is_in_while = True

            if is_in_while:
                last_node.next = next_node
                cur_node = next_node
                if not cur_node: break
                next_node = cur_node.next
            else:
                last_node = cur_node
                cur_node = next_node
                next_node = next_node.next
            
        return dummy.next
            