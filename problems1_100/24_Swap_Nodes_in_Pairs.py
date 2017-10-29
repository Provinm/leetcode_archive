# coding=utf-8
# author = zhouxin
# date = 2017.7.23

'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路:
        使用 双探针 逐一移动对相邻两个节点进行交换，考虑到移动头结点，增加一个伪节点在 head 之前
        举例：
        1 --> 2 --> 3
        # 增加伪结点和双探针
        -1(preprobe) --> 1(probe) --> 2 --> 3
        # 交换位置
        -1(preprobe) --> 2(probe) --> 1 --> 3
        # 移动探针到下下位
        -1 --> 2 --> 1(preprobe) --> 3(probe)
        # 依次循环
        # 注意退出条件 probe 为 none : 说明已到了尾节点
        # probe.next 为 none: 只剩下一个节点，不做处理
        """
        if not head or head.next is None: return head
        dummy = ListNode(-1)
        preprobe = dummy
        probe = head
        preprobe.next = probe

        while probe is not None and probe.next is not None:

            if probe is head:
                head = probe.next

            # 交换
            third = probe.next.next
            second = probe.next
            probe.next = third
            second.next = probe
            preprobe.next = second

            # 移动探针
            preprobe = preprobe.next.next
            probe = third


        return head
