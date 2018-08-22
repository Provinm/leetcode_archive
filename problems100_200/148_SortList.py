#coding=utf-8

'''

148. Sort List


Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


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

    return res

def print_node(node):
    return node.val

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        
        h, _ = self._sortList(head, None)
        return h

    def _sortList(self, head, tail):
        
        print(print_nodes(head), str(head), str(tail))
        if (not head) or head is tail:
            return head, tail

        cur = pivot = head
        pivot_eq = pivot
        while not cur is tail:

            tmp = cur.next
            if tmp and tmp.val < pivot.val:
                if tmp is tail:
                    tail = cur
                cur.next = tmp.next
                tmp.next = head
                head = tmp

            elif tmp and tmp.val == pivot.val:
                cur.next = tmp.next
                tmp.next = pivot.next
                pivot.next = tmp
                pivot = tmp
            
            else:
                cur = cur.next

        if pivot is pivot_eq:
            _h_tail = pivot.next
            link = None

        else:
            _h_tail = pivot.next
            link = pivot_eq.next

        pivot.next = None
        _h1, _t1 = self._sortList(head, pivot)
        _h2, _t2 = self._sortList(_h_tail, tail)

        if link:
            _t1.next = link
            pivot_eq.next = _h2

        else:
            _t1.next = _h2
        return _h1, _t2
            

if __name__ == "__main__":
    import random
    lst = list(range(10))
    random.shuffle(lst)
    lst = [1, 1, 2, 30, 8, 50, 3, 2]
    head = gen_list_nodes(lst)
    print_nodes(head)
    s = Solution()
    r = s.sortList(head)

    print("res = ", print_nodes(r))
    

            


        
        
