

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.prev = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.prev.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int):
        self.prev.next = ListNode(val=val, next=self.prev.next)
        self.size += 1

    def addAtTail(self, val: int):
        cur = self.prev
        for _ in range(self.size):
            cur = cur.next
        cur.next = ListNode(val=val)
        self.size += 1

    def addAtIndex(self, index: int, val: int):
        if index < 0 or index > self.size:
            return
        cur = self.prev
        for _ in range(index):
            cur = cur.next
        cur.next = ListNode(val=val, next=cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return
        cur = self.prev
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)