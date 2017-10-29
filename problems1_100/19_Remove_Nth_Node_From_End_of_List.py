# coding=utf-8
# author = zhouxin
# date = 2017.7.22

'''
19. Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        思路
        核心：在一次遍历中使用两个 探针 对链表进行操作，两指针差值为 n，
        所以，当 前指针 到达终点时， 后指针 指向被删除的节点的前一位。
        同时考虑到边界条件，比如去除的是头节点或者尾节点或者只有一个节点，
        使用一个 伪节点 添加到 头结点前面，便于操作。

        # 原链表
        1 --> 2 --> 3 --> 4 --> 5
        # 添加伪节点
        -1 --> 1 --> 2 --> 3 --> 4 --> 5
        # 定义两个探针
        -1(H/T) --> 1 --> 2 --> 3 --> 4 --> 5
        # H 探针向前移动 n 个节点 以2为例
        -1(T) --> 1 --> 2(H) --> 3 --> 4 --> 5
        # 此时 T / H 同时移动，直到 H 达到尾节点
        -1 --> 1 --> 2 --> 3(T) --> 4 --> 5(H)
        # 去除 倒数第 n 个节点
        -1 --> 1 --> 2 --> 3(T) --> 5(H)
        
        """

        dummy = ListNode(-1)
        dummy.next = head
        head_ = tail = dummy

        for i in range(n):
            head_ = head_.next

        # head_ = head_.next
        while head_.next is not None:
            head_ = head_.next
            tail = tail.next

        tail.next = tail.next.next

        return head
