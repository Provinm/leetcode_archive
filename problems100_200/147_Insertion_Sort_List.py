#coding=utf-8

'''

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def gen_list_nodes(lst):
    
    dummy_head = cur_node = ListNode(-1)
    for ele in lst:
        cur_node.next = ListNode(ele)
        cur_node = cur_node.next

    return dummy_head.next        
        
def print_nodes(head):
    
    res = []
    while head:
        res.append(head.val)
        head = head.next

    print(res)

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        min_node, max_node = None, None
        cur_node = head
        while cur_node:
            # 定义最小值
            if not min_node:
                min_node = cur_node
                cur_node = cur_node.next
            # define max node 
            elif not max_node:
                if cur_node.val > min_node.val:
                    max_node = cur_node
                else:
                    max_node = min_node
                    max_node.next = cur_node.next
                    min_node = cur_node
                    min_node.next = max_node
                    cur_node = cur_node.next
            else:
                
                if cur_node.val >= max_node.val:
                    max_node = cur_node
                    cur_node = cur_node.next

                elif cur_node.val <= min_node.val:
                    max_node.next = cur_node.next
                    cur_node.next = min_node
                    min_node = cur_node
                    cur_node = max_node.next

                else:
                    tmp_node = min_node
                    while True:
                        if tmp_node.next.val >= cur_node.val:
                            max_node.next = cur_node.next
                            cur_node.next = tmp_node.next
                            tmp_node.next = cur_node
                            cur_node = max_node.next
                            break
                        else:
                            tmp_node = tmp_node.next

        return min_node




            


