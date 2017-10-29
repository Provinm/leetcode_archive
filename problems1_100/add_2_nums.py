# coding=utf-8

'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''

# define linkedlist
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 记录新的节点
        prenode = None
        # 新链表的头节点
        firstNode = None
        # 是否进位
        is_add = 0
        while l1 is not None or l2 is not None:
            # 每次循环新建一个节点
            newl = ListNode(0)
            # 处理相加的值
            var_l1 = l1.val if l1 else 0
            var_l2 = l2.val if l2 else 0
            new_var = var_l1 + var_l2 + is_add
            is_add = 1 if new_var >= 10 else 0
            new_var = new_var % 10
            # 赋值到新节点
            newl.val = new_var
            # 移动节点记录位置
            if prenode is None:
                prenode = newl
                firstNode = newl
            else:
                prenode.next = newl
                prenode = prenode.next
            # 节点累加
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 处理特殊情况 比如[5] - [5] --- [0,1]
        if is_add == 1:
            newl = ListNode(1)
            prenode.next = newl
        return firstNode
