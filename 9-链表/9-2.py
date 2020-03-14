
class Solution:
    def FindKthToTail(self, head, k):
        n = self.GetLinkListLength(head)
        if n < k:
            return None

        for i in range(n-k):
            head = head.next
        return head

    def GetLinkListLength(self, head):
        if head is None:
            return 0

        count = 0
        while head:
            count += 1
            head = head.next
        return count
