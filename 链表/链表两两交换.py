# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp1 = current.next # 防止节点修改
            temp2 = current.next.next
            temp3 = current.next.next.next
            
            current.next = temp2
            current.next.next = temp1
            temp1.next = temp3
            current = temp2
        return dummy_head.next
