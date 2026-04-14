class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def remove_nth_from_end(head, n):
    dummy = ListNode()
    dummy.next = head
    
    slow = dummy
    fast = dummy
    
    for _ in range(n + 1):
        fast = fast.next
        
    while fast:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next


head = build_list([1,2,3,4,5])
print(to_list(remove_nth_from_end(head, 2)))   # [1,2,3,5]

head = build_list([1])
print(to_list(remove_nth_from_end(head, 1)))   # []

head = build_list([1,2])
print(to_list(remove_nth_from_end(head, 1)))   # [1]

head = build_list([1,2])
print(to_list(remove_nth_from_end(head, 2)))   # [2]

head = build_list([1,2,3])
print(to_list(remove_nth_from_end(head, 3)))   # [2,3]

head = build_list([1,2,3])
print(to_list(remove_nth_from_end(head, 1)))   # [1,2]

head = build_list([1,2,3,4])
print(to_list(remove_nth_from_end(head, 4)))   # [2,3,4]