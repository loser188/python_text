# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new_Head=ListNode(0)
        returnHead=new_Head
        while list1 and list2:
            if list1.val<=list2.val:
                new_Head.next=list1
                new_Head=new_Head.next
                list1=list1.next
            else:
                new_Head.next=list2
                new_Head=new_Head.next
                list2 =list2.next
        if list1:
            new_Head.next=list1
        else:
            new_Head.next=list2

        return returnHead.next

